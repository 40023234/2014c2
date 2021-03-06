import cherrypy

# 這是 C2G7 類別的定義
class C2G7(object):
    # 各組利用 index 引導隨後的程式執行
    @cherrypy.expose
    def index(self, *args, **kwargs):
        outstring = '''
這是 2014C2 協同專案下的 c2g7 分組程式開發網頁, 以下為 W12 的任務執行內容.<br />
<!-- 這裡採用相對連結, 而非網址的絕對連結 (這一段為 html 註解) -->
<a href="fillpoly">c2g7 fillpoly 繪圖</a><br />
<a href="drawline">c2g7 drawline 繪圖</a><br />
<a href="square">c2g7 square 繪圖</a><br />
<a href="flag">c2g7 flag 繪圖</a><br />
<a href="triangle">c2g7 triangle 繪圖</a><br />
<a href="triangle2">c2g7 triangle2 繪圖</a><br />
<a href="japan">c2g7 japan 繪圖</a><br />
<a href="USA">c2g7 USA 繪圖</a><br />
<a href="American_flagc2_1 ">c2g7 American_flagc2_1  繪圖</a><br />
<a href="American_flagc2_2 ">c2g7 American_flagc2_2  繪圖</a><br />
<a href="American_flagc2_3 ">c2g7 American_flagc2_3  繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A12%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A11%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A3%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=%23%20%E5%88%A9%E7%94%A8%E4%B8%89%E5%80%8B%E5%B7%A6%E8%BD%89%2C%20%E5%AE%9A%E7%BE%A9%E5%8F%B3%E8%BD%89%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)%0A%20%0A%23%20%E5%88%A9%E7%94%A8%E5%B7%A6%E5%8F%B3%E8%BD%89%E8%88%87%E5%89%8D%E9%80%B2%E5%AE%9A%E7%BE%A9%E8%B7%A8%E6%AC%84%E5%8B%95%E4%BD%9C%0Adef%20jump_over_hurdle()%3A%0A%20%20%20%20turn_left()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_left()%0A%20%20%20%0Amove()%0Ajump_over_hurdle()%0Ajump_over_hurdle()%0Ajump_over_hurdle()%0Amove()%0Ajump_over_hurdle()%0Ajump_over_hurdle()%0Ajump_over_hurdle()%0Amove()%0Ajump_over_hurdle()%0Amove()%0A&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0A%0A">c2g7 w15_1 繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A12%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A11%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A3%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=%23%20%E5%88%A9%E7%94%A8%E4%B8%89%E5%80%8B%E5%B7%A6%E8%BD%89%2C%20%E5%AE%9A%E7%BE%A9%E5%8F%B3%E8%BD%89%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)%0A%20%0A%23%20%E5%88%A9%E7%94%A8%E5%B7%A6%E5%8F%B3%E8%BD%89%E8%88%87%E5%89%8D%E9%80%B2%E5%AE%9A%E7%BE%A9%E8%B7%A8%E6%AC%84%E5%8B%95%E4%BD%9C%0Adef%20jump_over_hurdle()%3A%0A%20%20%20%20turn_left()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_left()%0A%20%20%20%0Amove()%0Ajump_over_hurdle()%0Ajump_over_hurdle()%0Ajump_over_hurdle()%0Amove()%0Ajump_over_hurdle()%0Ajump_over_hurdle()%0Ajump_over_hurdle()%0Amove()%0Ajump_over_hurdle()%0Amove()%0A&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0A%0A">c2g7 w15_2 繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A1%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A1%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A0%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%2C%223%2C1%22%3A%5B%22east%22%5D%2C%227%2C1%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=%23%20%E5%88%A9%E7%94%A8%E4%B8%89%E5%80%8B%E5%B7%A6%E8%BD%89%2C%20%E5%AE%9A%E7%BE%A9%E5%8F%B3%E8%BD%89%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)%0A%0A%23%20%E8%B7%AF%E5%BE%91%E8%A6%8F%E5%8A%83%E7%9B%B4%E5%88%B0%E5%88%B0%E9%81%94%E7%9B%AE%E7%9A%84%E5%9C%B0%E7%82%BA%E6%AD%A2%0Awhile%20(at_goal()%20%3D%3D%20False)%3A%0A%20%20%20%20%23%20%E5%88%A4%E6%96%B7%E5%8F%B3%E6%96%B9%E6%B2%92%E6%9C%89%E9%9A%9C%E7%A4%99%2C%20%E5%8F%B3%E8%BD%89%E4%B8%80%E6%AD%A5%0A%20%20%20%20if%20(right_is_clear()%20%3D%3D%20True)%3A%0A%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%23%20%E5%88%A4%E6%96%B7%E5%89%8D%E6%96%B9%E6%B2%92%E6%9C%89%E9%9A%9C%E7%A4%99%E7%89%A9%2C%20%E5%89%8D%E9%80%B2%E4%B8%80%E6%AD%A5%0A%20%20%20%20%20%20%20%20if%20(front_is_clear()%20%3D%3D%20True)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E4%B8%8D%E8%83%BD%E5%90%91%E5%8F%B3%E8%BD%89%2C%20%E4%B8%8D%E8%83%BD%E5%90%91%E5%89%8D%E9%80%B2%2C%20%E5%89%87%E5%90%91%E5%B7%A6%E8%BD%89%0A%20%20%20%20%20%20%20%20%20%20%20%20turn_left()%0A%0A%23%E5%8F%83%E8%80%83%E7%AC%ACc2g19%E7%9A%84%E7%A8%8B%E5%BC%8F%0A%0A%23(%E4%B8%80)%E9%81%A9%E7%94%A8%E9%97%9C%E5%8D%A1%EF%BC%9AHurdles%201~4%0A%23(%E4%BA%8C)%E8%A7%A3%E9%A1%8C%E9%81%8E%E7%A8%8B%EF%BC%9A%0A%20%20%20%23(1)%E7%9B%AE%E6%A8%99%3A%E8%A8%AD%E8%A8%88%E7%A8%8B%E5%BC%8F%E8%83%BD%E9%80%9A%E9%81%8E%E4%B8%8D%E5%90%8C%E7%9A%84%E9%9A%9C%E7%A4%99%0A%20%20%20%23(2)%E5%BF%83%E5%BE%97%EF%BC%9A%E4%BF%AE%E6%94%B9%E8%A8%B1%E5%A4%9A%E6%AC%A1%E8%B7%AF%E5%BE%91%EF%BC%8C%E7%99%BC%E5%85%88%E8%A6%81%E5%AF%AB%E4%B8%80%E5%80%8B%E5%A5%BD%E7%9A%84%E7%A8%8B%E5%BC%8F%E7%9C%9F%E7%9A%84%E4%B8%8D%E7%B0%A1%E5%96%AE&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g7 w15_3 繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A1%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A1%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A0%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%2C%223%2C1%22%3A%5B%22east%22%5D%2C%227%2C1%22%3A%5B%22east%22%5D%2C%223%2C2%22%3A%5B%22east%22%5D%2C%226%2C2%22%3A%5B%22east%22%5D%2C%227%2C2%22%3A%5B%22east%22%5D%2C%227%2C3%22%3A%5B%22east%22%5D%2C%2210%2C2%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=%23%20%E5%88%A9%E7%94%A8%E4%B8%89%E5%80%8B%E5%B7%A6%E8%BD%89%2C%20%E5%AE%9A%E7%BE%A9%E5%8F%B3%E8%BD%89%0Adef%20turn_right()%3A%0A%20%20%20%20for%20i%20in%20range(3)%3A%0A%20%20%20%20%20%20%20%20turn_left()%0A%0A%23%20%E8%B7%AF%E5%BE%91%E8%A6%8F%E5%8A%83%E7%9B%B4%E5%88%B0%E5%88%B0%E9%81%94%E7%9B%AE%E7%9A%84%E5%9C%B0%E7%82%BA%E6%AD%A2%20%20%20%20%20%20%20%20%0Awhile%20not%20at_goal()%3A%0A%20%20%20%23%20%E5%88%A4%E6%96%B7%E5%8F%B3%E6%96%B9%E6%B2%92%E6%9C%89%E9%9A%9C%E7%A4%99%2C%20%E5%8F%B3%E8%BD%89%E4%B8%80%E6%AD%A5%20%0A%20%20%20%20if%20not%20right_is_clear()%20and%20front_is_clear()%3A%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%23%20%E5%88%A4%E6%96%B7%E5%89%8D%E6%96%B9%E6%B2%92%E6%9C%89%E9%9A%9C%E7%A4%99%E7%89%A9%2C%20%E5%89%8D%E9%80%B2%E4%B8%80%E6%AD%A5%20%20%20%20%0A%20%20%20%20elif%20right_is_clear()%3A%0A%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%23%20%E4%B8%8D%E8%83%BD%E5%90%91%E5%8F%B3%E8%BD%89%2C%20%E4%B8%8D%E8%83%BD%E5%90%91%E5%89%8D%E9%80%B2%2C%20%E5%89%87%E5%90%91%E5%B7%A6%E8%BD%89%0A%20%20%20%20%20%20%20%20turn_left()&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0A%0A">c2g7 w16_1 繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A1%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A1%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A0%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%2C%223%2C1%22%3A%5B%22east%22%5D%2C%227%2C1%22%3A%5B%22east%22%5D%2C%223%2C2%22%3A%5B%22east%22%5D%2C%226%2C2%22%3A%5B%22east%22%5D%2C%227%2C2%22%3A%5B%22east%22%5D%2C%227%2C3%22%3A%5B%22east%22%5D%2C%2210%2C2%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=%23%20%E5%88%A9%E7%94%A8%E4%B8%89%E5%80%8B%E5%B7%A6%E8%BD%89%2C%20%E5%AE%9A%E7%BE%A9%E5%8F%B3%E8%BD%89%0Adef%20turn_right()%3A%0A%20%20%20%20for%20i%20in%20range(3)%3A%0A%20%20%20%20%20%20%20%20turn_left()%0A%0A%23%20%E8%B7%AF%E5%BE%91%E8%A6%8F%E5%8A%83%E7%9B%B4%E5%88%B0%E5%88%B0%E9%81%94%E7%9B%AE%E7%9A%84%E5%9C%B0%E7%82%BA%E6%AD%A2%20%20%20%20%20%20%20%20%0Awhile%20not%20at_goal()%3A%0A%20%20%20%23%20%E5%88%A4%E6%96%B7%E5%8F%B3%E6%96%B9%E6%B2%92%E6%9C%89%E9%9A%9C%E7%A4%99%2C%20%E5%8F%B3%E8%BD%89%E4%B8%80%E6%AD%A5%20%0A%20%20%20%20if%20not%20right_is_clear()%20and%20front_is_clear()%3A%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%23%20%E5%88%A4%E6%96%B7%E5%89%8D%E6%96%B9%E6%B2%92%E6%9C%89%E9%9A%9C%E7%A4%99%E7%89%A9%2C%20%E5%89%8D%E9%80%B2%E4%B8%80%E6%AD%A5%20%20%20%20%0A%20%20%20%20elif%20right_is_clear()%3A%0A%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%23%20%E4%B8%8D%E8%83%BD%E5%90%91%E5%8F%B3%E8%BD%89%2C%20%E4%B8%8D%E8%83%BD%E5%90%91%E5%89%8D%E9%80%B2%2C%20%E5%89%87%E5%90%91%E5%B7%A6%E8%BD%89%0A%20%20%20%20%20%20%20%20turn_left()&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0A%0A">c2g7 w16_2 繪圖</a><br />
'''
        return outstring

    # 以下為 c2g7 組所建立的 CherryPy 程式方法, 這裡的 fillpoly 利用 Brython 執行網際繪圖
    ''' 
    假如採用下列規畫
    
    import programs.c2g7 as c2g7
    root.c2g7 = c2g7.C2G7()
    
    則程式啟動後, 可以利用 /c2g7/fillpoly 呼叫函式執行
    '''
    @cherrypy.expose
    def fillpoly(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.3-20140704-213726/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入數學模組的所有方法
    from math import *
    # 導入時間模組
    import time
    # 導入 doc
    from browser import doc

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")

    # 定義座標轉換(0, 0) 到 (75, 20)
    def change_ref_system(x, y):
        return (20 + x * 8, 420 - y * 20)

    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    def fill():
        ctx.beginPath()
        ctx.moveTo(75,50)
        ctx.lineTo(100,75)
        ctx.lineTo(100,25)
        ctx.fill()
        
    def star():
        ctx.beginPath()
        ctx.moveTo(0,50)
        ctx.lineTo(11,16)
        ctx.lineTo(48,16)
        ctx.fill()

    ctx.fillStyle = "blue"
    fill()
    star()

    x1, y1 = change_ref_system(0, 0)
    for 索引 in range(0, 70, 4):
        x2, y2 = change_ref_system(索引, 20)
        draw_line(x1, y1, x2, y2, linethick=3, color="blue")
    x1, y1 = change_ref_system(70, 0)
    for 索引 in range(0, 70, 4):
        x2, y2 = change_ref_system(索引, 20)
        draw_line(x1, y1, x2, y2, linethick=3, color="red")
    </script>
    </body>
    </html>
    '''
        return outstring
    ''' 
    假如採用下列規畫
    
    import programs.c2g7 as c2g7
    root.c2g7 = c2g7.C2G7()
    
    則程式啟動後, 可以利用 /c2g1/drawline 呼叫函式執行
    '''
    @cherrypy.expose
    def drawline(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.3-20140704-213726/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")

    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    draw_line(0, 0, 100, 100)
    
    </script>
    </body>
    </html>
    '''
        return outstring
    ''' 
    假如採用下列規畫
    
    import programs.c2g7 as c2g7
    root.c2g7 = c2g7.C2G7()
    
    則程式啟動後, 可以利用 /c2g1/drawline 呼叫函式執行
    '''
    @cherrypy.expose
    def square(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.3-20140704-213726/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 800 光點
    ctx.setTransform(1, 0, 0, -1, 0, 800)

    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    draw_line(300, 300, 500, 300)
    draw_line(300, 300, 300, 500)
    draw_line(500, 300, 500, 500)
    draw_line(300, 500, 500, 500)
    
    </script>
    </body>
    </html>
    '''
        return outstring
        
    ''' 
    假如採用下列規畫
    
    import programs.c2g7 as c2g7
    root.c2g7 = c2g7.C2G7()
    
    則程式啟動後, 可以利用 /c2g1/drawline 呼叫函式執行
    '''
    @cherrypy.expose
    def flag(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.3-20140704-213726/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 800 光點
    ctx.setTransform(1, 0, 0, -1, 0, 800)

    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "red"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    draw_line(400, 500, 422.45, 430.9)
    draw_line(422.45, 430.9, 495.1, 430.9)
    draw_line(495.1, 430.9, 436.32, 388.19)
    draw_line(436.32, 388.19, 458.77, 319.09)
    draw_line(458.77, 319.09, 399.99, 361.8)
    draw_line(399.99, 361.8, 341.21, 319.09)
    draw_line(341.21, 319.09, 363.66, 388.19)
    draw_line(363.66, 388.19, 304.88, 430.9)
    draw_line(304.88, 430.9, 377.53, 430.9)
    draw_line(377.53, 430.9, 400, 500)

    
    </script>
    </body>
    </html>
    '''
        return outstring
        
        
    ''' 
    假如採用下列規畫
    
    import programs.c2g7 as c2g7
    root.c2g7 = c2g7.C2G7()
    
    則程式啟動後, 可以利用 /c2g1/drawline 呼叫函式執行
    '''
    @cherrypy.expose
    def triangle(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.3-20140704-213726/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 800 光點
    ctx.setTransform(1, 0, 0, -1, 0, 800)

    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "blue"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    draw_line(100, 100, 150, 250)
    draw_line(150, 250, 400, 400)
    draw_line(400, 400, 100, 100)

    
    </script>
    </body>
    </html>
    '''
        return outstring
        
        
    ''' 
    假如採用下列規畫
    
    import programs.c2g7 as c2g7
    root.c2g7 = c2g7.C2G7()
    
    則程式啟動後, 可以利用 /c2g1/drawline 呼叫函式執行
    '''
    @cherrypy.expose
    def triangle2(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.3-20140704-213726/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 800 光點
    ctx.setTransform(1, 0, 0, -1, 0, 800)

    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "blue"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()
        
# x, y 為中心,  r 為半徑, angle 旋轉角,  solid 空心或實心,  color 顏色

 # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "blue"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()
    def full():
        ctx.beginPath()
        ctx.moveTo(100,100)
        ctx.lineTo(150,250)
        ctx.lineTo(400,400)
        ctx.lineTo(100,100)
        ctx.fill()
        
    ctx.fillStyle = "red"
    full()



    
    </script>
    </body>
    </html>
    '''
        return outstring
        



    ''' 
    假如採用下列規畫
    
    import programs.c2g7 as c2g7
    root.c2g7 = c2g7.C2G7()
    
    則程式啟動後, 可以利用 /c2g1/drawline 呼叫函式執行
    '''
    @cherrypy.expose
    def japan(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript"        src="/static/Brython2.1.3-20140704-213726/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="300" height="200"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc
    import math

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 canvas.height 單位光點
    # ctx.setTransform(1, 0, 0, -1, 0, canvas.height)
    # 以下採用 canvas 原始座標繪圖
    flag_w = canvas.width
    flag_h = canvas.height
    circle_x = flag_w/2
    circle_y = flag_h/2

    # 先畫白
    ctx.fillStyle= 'black'
    ctx.fillRect(0,0,flag_w,flag_h)
    ctx.fillStyle= 'white'
    ctx.fillRect(0,0,flag_w-10,flag_h-10)
    # 白日:red心
    ctx.beginPath()
    ctx.arc(circle_x, circle_y, flag_w/8, flag_h/8, math.pi*2 ,  true)
    ctx.closePath()
    # 填色設為red
    ctx.fillStyle = 'red'
    ctx.fill()
    
    </script>
    </body>
    </html>
    '''
        return outstring
        

    ''' 
    假如採用下列規畫
    
    import programs.c2g7 as c2g7
    root.c2g7 = c2g7.C2G7()
    
    則程式啟動後, 可以利用 /c2g1/drawline 呼叫函式執行
    '''
 
    @cherrypy.expose
    def USA(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.3-20140704-213726/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc
    import math

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 800 光點
    ctx.setTransform(1, 0, 0, -1, 0, 800)



    # x, y 為中心,  r 為半徑, angle 旋轉角,  solid 空心或實心,  color 顏色
    def star(x, y, r, angle=0, solid=False, color="white"):
        # 以 x, y 為圓心, 計算五個外點
        deg = math.pi/180
        # 圓心到水平線距離
        a = r*math.cos(72*deg)
        # a 頂點向右到內點距離
        b = (r*math.cos(72*deg)/math.cos(36*deg))*math.sin(36*deg)
        # 利用畢氏定理求內點半徑
        rin = math.sqrt(a**2 + b**2)
        # 查驗 a, b 與 rin
        #print(a, b, rin)
        if(solid):
            ctx.beginPath()
        for i in range(5):
            xout = (x + r*math.sin(72*deg*i+angle*deg))
            yout = (y + r*math.cos(72*deg*i+angle*deg))
            # 外點增量 + 1
            xout2 = x + r*math.sin(72*deg*(i+1)+angle*deg)
            yout2 = y + r*math.cos(72*deg*(i+1)+angle*deg)
            xin = x + rin*math.sin(72*deg*i+36*deg+angle*deg)
            yin = y + rin*math.cos(72*deg*i+36*deg+angle*deg)
            # 查驗外點與內點座標
            #print(xout, yout, xin, yin)
            if(solid):
                # 填色
                if(i==0):
                    ctx.moveTo(xout, yout)
                    ctx.lineTo(xin, yin)
                    ctx.lineTo(xout2, yout2)
                else:
                    ctx.lineTo(xin, yin)
                    ctx.lineTo(xout2, yout2)
        if(solid):
            ctx.fillStyle = 'white'
            ctx.fill()

    for i in range(7):
        ctx.fillStyle='rgb(255, 0, 0)'
        ctx.fillRect(0, 0+40*i, 390, 20)

    ctx.fillStyle='rgb(0, 0, 149)'
    ctx.fillRect(0, 120, 210, 140)

    for i in range(6):
        for j in range(5):
            star(20+34*i, 134+28*j, 8, 0, True, "white")
    for i in range(5):
        for j in range(4):
            star(36+34*i, 148+28*j, 8, 0, True, "white")
    
    </script>
    </body>
    </html>
    '''
        return outstring
        
    @cherrypy.expose
    def American_flagc2_1 (self, *args, **kwargs):
        '''
        原始程式來源: http://blog.roodo.com/esabear/archives/19215194.html
        改寫為 Brython 程式
        '''
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.3-20140704-213726/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc
    import math

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 canvas.height 單位光點
    ctx.setTransform(1, 0, 0, -1,0,0)
    ctx.rotate(270*math.pi/180)
    # ctx.setTransform(1, 0, 0, -1, 0, canvas.height)
    # 以下採用 canvas 原始座標繪圖
    flag_w =380
    flag_h =200
    circle_x = flag_w/4
    circle_y = flag_h/4
    # 先畫滿地紅
    ctx.fillStyle= '#fff'
    ctx.fillRect(0,0,flag_w,flag_h)
    #長條紅線
    ctx.fillRect(0,0,flag_w,flag_h/13)
    ctx.fillStyle= 'rgb(255, 0, 0)'
    for i in range(0,flag_h,2*flag_h/13):
        b=i
        ctx.fillRect(0,b,flag_w,flag_h/13)
        ctx.fillStyle= 'rgb(255, 0, 0)'
        ctx.fill()
    # 先畫滿青天
    ctx.fillStyle='rgb(0, 0, 150)'
    ctx.fillRect(0,0,2*flag_w/5,7*flag_h/13)
    #星星白色
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()
    
    # x, y 為中心,  r 為半徑, angle 旋轉角,  solid 空心或實心,  color 顏色
    def star(x, y, r, angle=0, solid=False, color="#f00"):
        # 以 x, y 為圓心, 計算五個外點
        deg = math.pi/180
        # 圓心到水平線距離
        a = r*math.cos(72*deg)
        # a 頂點向右到內點距離
        b = (r*math.cos(72*deg)/math.cos(36*deg))*math.sin(36*deg)
        # 利用畢氏定理求內點半徑
        rin = math.sqrt(a**2 + b**2)
        # 查驗 a, b 與 rin
        #print(a, b, rin)
        if(solid):
            ctx.beginPath()
        for i in range(5):
            xout = (x + r*math.sin((360/5)*deg*i+angle*deg))
            yout = (y + r*math.cos((360/5)*deg*i+angle*deg))
            # 外點增量 + 1
            xout2 = x + r*math.sin((360/5)*deg*(i+1)+angle*deg)
            yout2 = y + r*math.cos((360/5)*deg*(i+1)+angle*deg)
            xin = x + rin*math.sin((360/5)*deg*i+36*deg+angle*deg)
            yin = y + rin*math.cos((360/5)*deg*i+36*deg+angle*deg)
            # 查驗外點與內點座標
            #print(xout, yout, xin, yin)
            if(solid):
                # 填色
                if(i==0):
                    ctx.moveTo(xout, yout)
                    ctx.lineTo(xin, yin)
                    ctx.lineTo(xout2, yout2)
                else:
                    ctx.lineTo(xin, yin)
                    ctx.lineTo(xout2, yout2)
            else:
                # 空心
                draw_line(xout, yout, xin, yin, color)
                # 畫空心五芒星, 無關畫線次序, 若實心則與畫線次序有關
                draw_line(xout2, yout2, xin, yin, color)
        if(solid):
            ctx.fillStyle = color
            ctx.fill()
    #star(100, 100, 50, 0, False, "#000")
    for i in range(5):
        for j in range(4):
            star(24+24*i, 24+22*j, 5, 0, true, "#fff")
    for i in range(6):
        for j in range(5):
            star(12+24*i, 12+22*j, 5, 0, true, "#fff")

    </script>
    </body>
    </html>
    '''
        return outstring
    @cherrypy.expose
    def American_flagc2_2 (self, *args, **kwargs):
        '''
        原始程式來源: http://blog.roodo.com/esabear/archives/19215194.html
        改寫為 Brython 程式
        '''
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.3-20140704-213726/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc
    import math

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 canvas.height 單位光點
    ctx.setTransform(1, 0, 0, -1,0,0)
    ctx.rotate(270*math.pi/180)
    # ctx.setTransform(1, 0, 0, -1, 0, canvas.height)
    # 以下採用 canvas 原始座標繪圖
    flag_w =300
    flag_h =200
    circle_x = flag_w/4
    circle_y = flag_h/4
    # 先畫滿地紅
    ctx.fillStyle= '#fff'
    ctx.fillRect(0,0,flag_w,flag_h)
    #長條紅線
    ctx.fillRect(0,0,flag_w,flag_h/13)
    ctx.fillStyle= 'rgb(255, 0, 0)'
    for i in range(0,flag_h,2*flag_h/13):
        b=i
        ctx.fillRect(0,b,flag_w,flag_h/13)
        ctx.fillStyle= 'rgb(255, 0, 0)'
        ctx.fill()
    # 先畫滿青天
    ctx.fillStyle='rgb(0, 0, 150)'
    ctx.fillRect(0,0,2*flag_w/5,7*flag_h/13)
    #星星白色
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()
    
    # x, y 為中心,  r 為半徑, angle 旋轉角,  solid 空心或實心,  color 顏色
    def star(x, y, r, angle=0, solid=False, color="#f00"):
        # 以 x, y 為圓心, 計算五個外點
        deg = math.pi/180
        # 圓心到水平線距離
        a = r*math.cos(72*deg)
        # a 頂點向右到內點距離
        b = (r*math.cos(72*deg)/math.cos(36*deg))*math.sin(36*deg)
        # 利用畢氏定理求內點半徑
        rin = math.sqrt(a**2 + b**2)
        # 查驗 a, b 與 rin
        #print(a, b, rin)
        if(solid):
            ctx.beginPath()
        for i in range(5):
            xout = (x + r*math.sin((360/5)*deg*i+angle*deg))
            yout = (y + r*math.cos((360/5)*deg*i+angle*deg))
            # 外點增量 + 1
            xout2 = x + r*math.sin((360/5)*deg*(i+1)+angle*deg)
            yout2 = y + r*math.cos((360/5)*deg*(i+1)+angle*deg)
            xin = x + rin*math.sin((360/5)*deg*i+36*deg+angle*deg)
            yin = y + rin*math.cos((360/5)*deg*i+36*deg+angle*deg)
            # 查驗外點與內點座標
            #print(xout, yout, xin, yin)
            if(solid):
                # 填色
                if(i==0):
                    ctx.moveTo(xout, yout)
                    ctx.lineTo(xin, yin)
                    ctx.lineTo(xout2, yout2)
                else:
                    ctx.lineTo(xin, yin)
                    ctx.lineTo(xout2, yout2)
            else:
                # 空心
                draw_line(xout, yout, xin, yin, color)
                # 畫空心五芒星, 無關畫線次序, 若實心則與畫線次序有關
                draw_line(xout2, yout2, xin, yin, color)
        if(solid):
            ctx.fillStyle = color
            ctx.fill()
    #star(100, 100, 50, 0, False, "#000")
    for i in range(5):
        for j in range(4):
            star(20+20*i, 20+20*j, 5, 0, true, "#fff")
    for i in range(6):
        for j in range(5):
            star(10+20*i, 10+20*j, 5, 0, true, "#fff")
    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    ctx.setTransform(1, 0, 0, -1,300,0)
    ctx.rotate(270*math.pi/180)
    # 進行座標轉換, x 軸不變, y 軸反向且移動 canvas.height 單位光點
    # ctx.setTransform(1, 0, 0, -1, 0, canvas.height)
    # 以下採用 canvas 原始座標繪圖
    circle_x = flag_w/4
    circle_y = flag_h/4
    # 先畫滿地紅
    ctx.fillStyle='rgb(255, 0, 0)'
    ctx.fillRect(0,0,flag_w,flag_h)
    # 再畫青天
    ctx.fillStyle='rgb(0, 0, 150)'
    ctx.fillRect(0,0,flag_w/2,flag_h/2)
    # 畫十二到光芒白日
    ctx.beginPath()
    star_radius = flag_w/8
    angle = 0
    for i in range(24):
        angle += 5*math.pi*2/12
        toX = circle_x + math.cos(angle)*star_radius
        toY = circle_y + math.sin(angle)*star_radius
        # 只有 i 為 0 時移動到 toX, toY, 其餘都進行 lineTo
        if (i):
            ctx.lineTo(toX, toY)
        else:
            ctx.moveTo(toX, toY)
    # 將填色設為白色
    ctx.fillStyle = '#fff'
    ctx.fill()
    # 白日:藍圈
    ctx.beginPath()
    # 查詢 canvas arc 如何定義
    ctx.arc(circle_x, circle_y, flag_w*17/240, 0, math.pi*2, true)
    ctx.closePath()
    # 填色設為藍色
    ctx.fillStyle = 'rgb(0, 0, 149)'
    ctx.fill()
    # 白日:白心
    ctx.beginPath()
    ctx.arc(circle_x, circle_y, flag_w/16, 0, math.pi*2, true)
    ctx.closePath()
    # 填色設為白色
    ctx.fillStyle = '#fff'
    ctx.fill()

    </script>
    </body>
    </html>
    '''
        return outstring
    @cherrypy.expose
    def American_flagc2_3 (self, *args, **kwargs):
        '''
        原始程式來源: http://blog.roodo.com/esabear/archives/19215194.html
        改寫為 Brython 程式
        '''
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.3-20140704-213726/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc
    import math

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 canvas.height 單位光點
    ctx.setTransform(1, 0, 0, -1,550/2-190,550/2-100)
    ctx.rotate(315*math.pi/180)
    # ctx.setTransform(1, 0, 0, -1, 0, canvas.height)
    # 以下採用 canvas 原始座標繪圖
    flag_w =380
    flag_h =200
    circle_x = flag_w/4
    circle_y = flag_h/4
    # 先畫滿地紅
    ctx.fillStyle= '#fff'
    ctx.fillRect(0,0,flag_w,flag_h)
    #長條紅線
    ctx.fillRect(0,0,flag_w,flag_h/13)
    ctx.fillStyle= 'rgb(255, 0, 0)'
    for i in range(0,flag_h,2*flag_h/13):
        b=i
        ctx.fillRect(0,b,flag_w,flag_h/13)
        ctx.fillStyle= 'rgb(255, 0, 0)'
        ctx.fill()
    # 先畫滿青天
    ctx.fillStyle='rgb(0, 0, 150)'
    ctx.fillRect(0,0,2*flag_w/5,7*flag_h/13)
    #星星白色
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()
    
    # x, y 為中心,  r 為半徑, angle 旋轉角,  solid 空心或實心,  color 顏色
    def star(x, y, r, angle=0, solid=False, color="#f00"):
        # 以 x, y 為圓心, 計算五個外點
        deg = math.pi/180
        # 圓心到水平線距離
        a = r*math.cos(72*deg)
        # a 頂點向右到內點距離
        b = (r*math.cos(72*deg)/math.cos(36*deg))*math.sin(36*deg)
        # 利用畢氏定理求內點半徑
        rin = math.sqrt(a**2 + b**2)
        # 查驗 a, b 與 rin
        #print(a, b, rin)
        if(solid):
            ctx.beginPath()
        for i in range(5):
            xout = (x + r*math.sin((360/5)*deg*i+angle*deg))
            yout = (y + r*math.cos((360/5)*deg*i+angle*deg))
            # 外點增量 + 1
            xout2 = x + r*math.sin((360/5)*deg*(i+1)+angle*deg)
            yout2 = y + r*math.cos((360/5)*deg*(i+1)+angle*deg)
            xin = x + rin*math.sin((360/5)*deg*i+36*deg+angle*deg)
            yin = y + rin*math.cos((360/5)*deg*i+36*deg+angle*deg)
            # 查驗外點與內點座標
            #print(xout, yout, xin, yin)
            if(solid):
                # 填色
                if(i==0):
                    ctx.moveTo(xout, yout)
                    ctx.lineTo(xin, yin)
                    ctx.lineTo(xout2, yout2)
                else:
                    ctx.lineTo(xin, yin)
                    ctx.lineTo(xout2, yout2)
            else:
                # 空心
                draw_line(xout, yout, xin, yin, color)
                # 畫空心五芒星, 無關畫線次序, 若實心則與畫線次序有關
                draw_line(xout2, yout2, xin, yin, color)
        if(solid):
            ctx.fillStyle = color
            ctx.fill()
    #star(100, 100, 50, 0, False, "#000")
    for i in range(5):
        for j in range(4):
            star(24+24*i, 24+22*j, 5, 0, true, "#fff")
    for i in range(6):
        for j in range(5):
            star(12+24*i, 12+22*j, 5, 0, true, "#fff")

    </script>
    </body>
    </html>
    '''
        return outstring