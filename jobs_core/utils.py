import os

def WriteLog(pathNameOut, output):
    logFilename = os.path.join(os.getcwd(),  pathNameOut, 'log.txt')
    f = open(logFilename , 'w' )
    f.write(output)
    f.close()

def SendEmail(taskId, 
              output, 
              EmailServerLogin, 
              EmailServerLoginPass, 
              EmailSender, 
              EmailList):
    import smtplib
    email = "Tarea id = " + taskId + " Finalizada\n\nDetalle:\n\n__________" + output + "\n\n_________"
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(EmailServerLogin, EmailServerLoginPass)
    server.sendmail(
        EmailSender,
        EmailList,
        email)
    server.quit()
