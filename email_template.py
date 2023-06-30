def birthday_template(name):
    htmly = (
        """<!DOCTYPE html>
<html>
<head>
  <title>Birthday Wish Card</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f2f2f2;
      margin: 0;
      padding: 0;
      height: 300px;
    }
    
    .envelope {
      width: 400px;
      height: 500px;
      background-color: #292927;
      border: 2px solid #7b87f3;
      position: relative;
      margin: 50px auto;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
      padding: 20px;
    }
    
    .envelope:before {
      content: "";
      width: 380px;
      height: 40px;
      background-color: #66abc8;
      border-top: 2px solid #9174ef;
      position: absolute;
      top: -2px;
      left: 10px;
    }
    
    .envelope:after {
      content: "";
      width: 20px;
      height: 20px;
      background-color: #fafafa;
      border: 2px solid #e0e0e0;
      position: absolute;
      top: -10px;
      right: 10px;
      transform: rotate(45deg);
    }
    
    h1 {
      text-align: center;
      color: #ff4081;
      margin-bottom: 30px;
      color: white;
    }
    
    p {
      font-size: 18px;
      line-height: 1.5;
      color: #333333;
      color: white
    }
    
    .cake {
      text-align: center;
      margin-top: 30px;
    }
    
    .cake img {
      width: 200px;
      border-radius: 10px;
      margin-bottom: 10px;
    }
    
 
  </style>
</head>
<body>
  <div class="envelope">
    <h1>Happy Birthday!</h1>
    <p>Dear """
        + name
        + """,</p>
    <p>Wishing you a day filled with joy, laughter, and happiness on your special day. May all your dreams and wishes come true. Happy birthday!</p>
    <div class="cake">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Cartoon_Happy_Birthday_Cake.svg/800px-Cartoon_Happy_Birthday_Cake.svg.png" alt="Birthday Cake">
    </div>"""
    )

    return htmly
