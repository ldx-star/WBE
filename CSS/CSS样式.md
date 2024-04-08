# CSS样式

---

## 1、高度和宽度

```css
.C1{
	height:300px;
	width:50px;
}
```

注意事项：

* 宽度，支持百分比
* 行内标签：默认无效
* 块级标签：默认有效（霸道，右侧区域空白，也不给你占用）

![image-20240403155956480](/home/ldx/.config/Typora/typora-user-images/image-20240403155956480.png)

## 2、块级和行内标签

```CSS
        .c1 {
            display: inline-block;
            height: 300px;
            width: 100px;
            border: 1px solid red;
        }
行内标签：不能设置高度和边距
```

![image-20240403155909988](/home/ldx/.config/Typora/typora-user-images/image-20240403155909988.png)

## 3、字体和颜色

```CSS
    <style>
        .c1 {
            color: red; ->颜色
            font-size: 58px; ->大小
            font-weight: 600; ->加粗
            font-family: "Microsoft Yahei"; ->字体
        }
    </style>
```

![image-20240403162007506](/home/ldx/.config/Typora/typora-user-images/image-20240403162007506.png)

## 4、文字对齐方式

```CSS
        .c1 {
            height: 59px;
            width: 300px;
            border: 1px solid red;

            text-align: center; /* 水平方向居中 */
            line-height: 59px;  /* 垂直方向居中 */
        }
```

![image-20240403162830252](/home/ldx/.config/Typora/typora-user-images/image-20240403162830252.png)

## 5、浮动

```CSS
<div>
    <span>左边</span>
    <span style="float: right">右边</span>
</div>
```



![image-20240403163447644](/home/ldx/.config/Typora/typora-user-images/image-20240403163447644.png)

标签浮动起来后，就会脱离文档流。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1 {
            float: left;
            height: 100px;
            width: 300px;
            border: 1px solid red;
        }
    </style>
</head>
<body>
<div>
    <div class="c1"></div>
    <div class="c1"></div>
    <div class="c1"></div>
</div>
<div>你好呀！</div>
</body>
</html>
```

![image-20240403164318844](/home/ldx/.config/Typora/typora-user-images/image-20240403164318844.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1 {
            float: left;
            height: 100px;
            width: 300px;
            border: 1px solid red;
        }
    </style>
</head>
<body>
<div>
    <div class="c1"></div>
    <div class="c1"></div>
    <div class="c1"></div>
    <div style="clear:both;"></div> /* 解决方法 */
</div>
<div>你好呀！</div>
</body>
</html>
```

![image-20240403164452068](/home/ldx/.config/Typora/typora-user-images/image-20240403164452068.png)

## 6、内边距

```css
.outer{
    height: 200px;
    width: 200px;
    border: 1px solid red;

    padding-top: 20px;
    padding-left: 20px;
    padding-right: 20px;
}
```



![image-20240403165156734](/home/ldx/.config/Typora/typora-user-images/image-20240403165156734.png)

## 7、外边距

```html
<div style="height: 200px; background-color: dodgerblue;"></div>
<div style="background-color: aliceblue;height: 100px;margin-top: 20px"></div>
```

![image-20240403165800233](/home/ldx/.config/Typora/typora-user-images/image-20240403165800233.png)

