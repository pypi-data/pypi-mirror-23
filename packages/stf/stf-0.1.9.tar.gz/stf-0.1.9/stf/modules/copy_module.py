import sys
import os
import shutil
from stf.modules.base_module import STFBaseModule
from stf.lib.logging.logger import Logger

logger = Logger.getLogger(__name__)

class STFCopyModuleError(BaseException):
    """If error, raise it."""
    pass
class STFCopyModule(STFBaseModule):
    def __init__(self, pluginManager):
        super(STFCopyModule, self).__init__(pluginManager)

    def checkMode(self, mode):
        """
        TBD
        """
        pass
    
    def checkModeParameter(self, parameter):
        """
        TBD
        """
        pass
    
    def getlabs(self, lab_info):
        if lab_info:
            nodeName = lab_info.split("@")[1]
            userName = lab_info.split("@")[0]
            
            labs = self.variablePlugin.getLabInfo(nodeName, userName)
            if not labs:
                logger.error("there is no lab for %s  as %s" % (nodeName, userName))
                raise STFCopyModuleError("there is no lab for %s  as %s" % (nodeName, userName))
            return labs  
    
    def getlabdetailInfo(self,lab):
        account = lab.user
        passwd = lab.password
        ip = lab.IP
        becomeUser = lab.become_user
        becomePW = lab.become_password
        return account, passwd, ip, becomeUser, becomePW
        
    def checkLabs(self, labs):
        for lab in labs:
            account = lab.user
            passwd = lab.password
            ip = lab.IP
            becomeUser = lab.become_user
            becomePW = lab.become_password
            try:
                if not becomeUser:
                    self.sshManager.getClient(ip, user=account, pw=passwd)
                else:
                    self.sshManager.getClient(ip, account, passwd, becomeUser, becomePW)
            except BaseException, msg:
                 errorMsg = "cannot access to %s as user %s:%s, error msg is %s" % (ip, account, passwd, str(msg))
                 logger.error(errorMsg)
                 raise STFCopyModuleError(errorMsg)
            else:
                 raise STFCopyModuleError("not support jump host now")  
                 
    def checkModuleParameter(self, module, jumphost_info, lab_info):
        """
        :param module parameter
        """
        logger.info("module name is %s, justhost is %s,  access node is %s", module, jumphost_info, lab_info)
        if module.lower() != "copy":
            logger.error("this is copy module, not %s", module)
            raise STFCopyModuleError("this is copy module, not %s", module)
        if jumphost_info:
            logger.error("not support jump host now")
            raise STFCopyModuleError("not support jump host now") 
        if lab_info: 
            labs = self.getlabs(lab_info) 
            for lab in labs:
                account, passwd,ip,becomeUser,becomePW = self.getlabdetailInfo(lab)
                try:
                    if not becomeUser:
                        self.sshManager.getClient(ip, user=account, pw=passwd)
                    else:
                        self.sshManage(ip, account, passwd, becomeUser, becomePW)
                except BaseException, msg:
                     errorMsg = "cannot access to %s as user %s:%s, error msg is %s" % (ip, account, passwd, str(msg))
                     logger.error(errorMsg)
                     raise STFCopyModuleError(errorMsg)
       
    def checkTags(self, tags):
        pass
    
    def checkCaseIDs(self, cases):
        pass
    
    def checkOthers(self, f):
        pass
    
    def copyLocal(self, src, dst):
        try:
            if not os.path.exists(src):
                raise STFCopyModuleError("Source  %s does not exits" , src);
            if not os.path.isdir(dst):
                raise STFCopyModuleError("Target dir %s does not exits" , dst);
            if os.path.isdir(src):
                logger.info("copy local dir begin from %s to %s" ,src, dst)
                if src.endswith("/"):
                    src = src[:-1]
                srcbasename = os.path.basename(src)
                shutil.copy(src, os.path.join(dst, srcbasename))
            if os.path.isfile(src):
                
                if not dst.endswith("/"):
                    dst = dst + "/"
                logger.info("copy local file begin from %s to %s" ,src, dst)
                shutil.copy(src, dst)
        except Exception as err:
                logger.error("copy local from %s to %s fail, error msg is %s" , src, dst, err)
                rc = 255
                output = "copy fail"
        else:
            rc = 0
            output = "copy success"
            err = ""
                
        return rc, output, err
     
    def copyremote(self, src, dst, ip, account, pw, cpmode):
        
        try:
            if cpmode == "Download":
                #for dir and file
                logger.info("download from server %s , user is %s, %s to %s" , ip, account, src, dst);
                self.sshManager.scpGetDir(ip, src, account, dst, pw);
            
            if cpmode == "Upload":
                print "account is %s, pw is %s", account, pw
                logger.info("upload to server %s , user is %s, %s to %s" , ip, account, src, dst);
                self.sshManager.scpPutDirOrFile(src, dst, ip, account, pw)
        except Exception as err:
             logger.error("copy remote from %s to %s fail, , cp mode is %s, error msg is %s" , src, dst, cpmode, err)
             rc = 255
             output = "copy fail"
        else:
            rc = 0
            output = "copy success"
            err = ""
        return rc, output, err


    def run(self, caseInfo):
        caseFileLocation = caseInfo.current_step.path
        caseFileName = os.path.basename(caseFileLocation)
        mode = caseInfo.current_step.mode
        parameter = caseInfo.current_step.mode_argv 
        module = caseInfo.current_step.module
        jumphost_info = caseInfo.current_step.jumphost_info
        lab_info = caseInfo.current_step.lab_info
        tags = caseInfo.current_step.step_tags
        
#         casefile = self.appendExtToCaseFile(caseFileLocation)
        logger.info( "copycasefile is %s", caseFileLocation)
        #file content format: 
        #download :remotefile -> localdir
        #upload:   localdir -> :remotefilepath
        file = open(caseFileLocation)

        #initialize env
        env_cache = []
        for e in self.variablePlugin.options('Env'):
            if e not in os.environ:
                os.environ[e] = self.variablePlugin.getEnv(e)
                env_cache.append(e)


        for line in file:
            logger.debug("line in file is %s", line)
            linearray = line.strip("\n").split("->")
            src = linearray[0].strip()
            dst = linearray[1].strip()
            cpmode = ""
            if ":" in src and not ":" in dst:
                src = os.path.expandvars(src.split(":")[1])
                cpmode = "Download"
            elif ":" in dst and not ":" in src :
                dst = os.path.expandvars(dst.split(":")[1])
                cpmode = "Upload"
            elif not ":" in src and not ":" in dst:
                cpmode = "Local"
            else:
                cpmode = "Error"
            
            logger.debug("copy mode is %s", cpmode)

        
            if not lab_info and cpmode == "Local":
                    logger.debug("copy in local, src is %s, dst is %s", src, dst)
                    self.processStart(caseInfo, 0)
                    rc, output, errs = self.copyLocal(src, dst)
                    logger.debug("run copy %s  return code is %s, output is %s", caseFileName, rc, output)
                    self.processEnd(caseInfo, 0, caseFileName, rc, output, errs, 0)
            elif lab_info and  cpmode == "Upload" or cpmode == "Download":
                for lab in self.getlabs(lab_info):
                    account, passwd,ip,becomeUser,becomePW = self.getlabdetailInfo(lab)

                    self.processStart(caseInfo, 0)
                    rc, output, err = self.copyremote(src, dst, ip, account, passwd, cpmode)
                    self.processEnd(caseInfo, 0, caseFileName, rc, output, err, 0)
            else:
                logger.error("copy moudule error, lab in case file name not coordinate with case content")
                for e in env_cache:
                    del os.environ[e]

                raise STFCopyModuleError("copy moudule error, lab in case file name not coherent with case content")
                
        for e in env_cache:
            del os.environ[e]
        
    
           
        