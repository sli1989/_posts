## introduction

三种实现：
- python的smtplib
- javamail.lib
- 自己写简易socket实现
- telnet实现

## smtplib实现发送email

1. 利用smtplib发送email，源代码。

见song.common.autoalert.email.send.py:

    // 以python源代码为基准
    import smtplib  
    from email.mime.text import MIMEText  
    from config import *
    import socket
    
    def send_mail(to_list,subject,content):  
        me="hello"+"<"+mail_user+"@"+mail_postfix+">"  
        msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = ";".join(to_list)  
        try:  
            server = smtplib.SMTP()
            
            server.connect(smtp_host, smtp_port) # 这里有response吗？加ssl连接吗？
            server.ehlo()  # 与服务器打招呼，并告知客户端使用的机器名字，可以随便填写
            server.starttls() # 登录时需要启动TLS加密 (smtp服务器规定的)
            server.login(mail_user,mail_pass)  # 这里做了什么？建立了tls加密的socket连接，然后发送加密后的数据获取认证吗？
            server.sendmail(me, to_list, msg.as_string())  # 这里有response吗，没有response应该就是UDP连接吧 
            server.close()
            return True  
        except Exception, e:  
            print str(e)  
            return False  
        
    if __name__ == '__main__':  
        if send_mail(mailto_list,"hello","send from python smtplib"):  
            print "发送成功"  
        else:  
            print "发送失败"  


2. 修改源代码 smtpliba.py

'''

    def putcmd(self, cmd, args=""):
        """Send a command to the server."""
        if args == "":
            str = '%s%s' % (cmd, CRLF)
        else:
            str = '%s %s%s' % (cmd, args, CRLF)
        print 'sending:' + str  # 在smtpliba.py中添加这一行代码
        self.send(str)

3. 运行

'''
    
    // Authentication methods
    Authentication methods the server supports:
    authlist: ['LOGIN', 'PLAIN', 'XOAUTH2']  // outlook竟然还支持plain的登录方式？
    
    // authmethod = AUTH_PLAIN
    sending:ehlo [192.168.253.1]
    sending:STARTTLS
    sending:ehlo [192.168.253.1]
    sending:AUTH PLAIN AHMyamFja3NvbkBob3RtYWlsLmNvbQBrZGY4KmRmNSFzNF9q
    sending:mail FROM:<s2jackson@hotmail.com> size=215
    sending:rcpt TO:<13521649928@139.com>
    sending:data
    发送成功
    
    // authmethod = AUTH_LOGIN
    sending:ehlo [192.168.253.1]
    sending:STARTTLS
    sending:ehlo [192.168.253.1]
    sending:AUTH LOGIN czJqYWNrc29uQGhvdG1haWwuY29t
    sending:a2RmOCpkZjUhczRfag==
    sending:mail FROM:<s2jackson@hotmail.com> size=215
    sending:rcpt TO:<13521649928@139.com>
    sending:data
    发送成功


## javamail实现

    // 以java源代码为基准
    package song.net.mail.demo;
    
    import javax.mail.*;
    import javax.mail.internet.*;
    import javax.mail.Authenticator;
    import javax.mail.Message;
    import javax.mail.PasswordAuthentication;
    
    import java.util.Properties;
    
    import song.config.Info;
    
    public class SendWithAuth {
    
        private static final String SMTP_HOST_NAME = Info.SMTP_HOST;
        private static final Integer SMTP_PORT = Info.SMTP_PORT;
        private static final String SMTP_AUTH_USER = Info.SMTP_AUTH_USER;
        private static final String SMTP_AUTH_PWD  = Info.SMTP_AUTH_PWD;
        private static final String MAIL_TO  = Info.MAIL_TO;
    
        public static void main(String[] args) throws Exception{
           new SendWithAuth().test();
        }
    
        public void test() throws Exception{
            Properties props = new Properties();
            // property列表，见 https://javamail.java.net/nonav/docs/api/com/sun/mail/smtp/package-summary.html
            props.put("mail.transport.protocol", "smtp");
            props.put("mail.smtp.host", SMTP_HOST_NAME);
            props.put("mail.smtp.port", SMTP_PORT); // 默认是25端口，但是这个smtp服务器要求是587端口
            props.put("mail.smtp.auth", "true");
            props.put("mail.smtp.starttls.enable", true); //  登录时需要启动TLS加密 (smtp服务器规定的)
    
            Authenticator auth = new SMTPAuthenticator();
            Session mailSession = Session.getDefaultInstance(props, auth);
            Transport transport = mailSession.getTransport();
    
            // header是在什么时候加的？比如Subject，from，to, cc等
            MimeMessage message = new MimeMessage(mailSession);
            message.setContent("send from java mail", "text/plain"); // 等价于message.setText
            message.setFrom(new InternetAddress(SMTP_AUTH_USER)); // Set From: header field of the header.
            message.addRecipient(Message.RecipientType.TO,
                 new InternetAddress(MAIL_TO));  // Set To: header field of the header.
            message.setSubject("hi"); // Set Subject: header field， 可省略
            
            
            transport.connect();
            transport.sendMessage(message,
                message.getRecipients(Message.RecipientType.TO));
            transport.close();
        }
    
        private class SMTPAuthenticator extends javax.mail.Authenticator {
            public PasswordAuthentication getPasswordAuthentication() {
               String username = SMTP_AUTH_USER;
               String password = SMTP_AUTH_PWD;
               return new PasswordAuthentication(username, password);
            }
        }
    
    }





## 自己写简易socket实现smtp邮件发送

...

## telnet实现smtp邮件发送

...