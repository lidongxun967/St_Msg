import random
import string

def domain_split(input_string:str,port:int):
    parts = input_string.split(":")
    if len(parts) == 2:
        return parts[0], int(parts[1])
    elif len(parts) == 1:
        return parts[0], port
    else:
        return None

index = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>留言板</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 600px;
            margin: 20px auto;
            background-color: #ffffff;
            padding: 20px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 5px solid;
            border-image: linear-gradient(to right, #004377, #4ec1ff52);
            border-image-slice: 1;
            padding-bottom: 10px;
        }
        .logo {
            display: flex;
            align-items: center;
        }
        .logo img {
            max-width: 75px;
        }
        .logo-text {
            font-size: 24px;
            margin-left: 10px;
            color: #0077b6;
            font-weight: bold;
        }
        .contact {
            margin-top: 20px;
        }
        .contact p {
            margin: 10px 0;
        }
        .message {
            margin-top: 20px;
            padding-top: 10px;
        }
        .message-content {
            padding-top: 10px;
        }
        .reminder {
            margin-top: 20px;
            font-style: italic;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">
                <img src="data:image/jpeg;base64,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" alt="工作室Logo">
                <span class="logo-text">Debug-Epoch</span>
            </div>
            <div class="contact">
                <p>用户联系方式： <a>!User_Email!</a></p>
            </div>
        </div>
        <div class="message">
            <p>!User_Message!</p>
            <div class="message-content">
        </div>
        <div class="reminder">
            <p>本邮件为自动发送，回复信息不能与发送者交流。</p>
            <p>你收到此消息是因为你被管理员认为是该工作室管理员，如有疑问，联系 1985409711@qq.com</p>
        </div>
    </div>
</body>
</html>

"""
