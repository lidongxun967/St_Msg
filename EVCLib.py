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
            border-top: 5px solid;
            border-image: linear-gradient(to right, #4ec1ff52, #004377);
            border-image-slice: 1;
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
                <img src="https://destudio.streamlit.app/~/+/media/f7ee546e10e0f44a77eaa7c68620620163118b7f7c52d7c89284f0e7.jpg" alt="工作室Logo">
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
