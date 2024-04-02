# HTML

---

## 1、标题

```html
<h1>一级标题</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>
<h4>四级标题</h4>
```

![image-20240401202336790](/home/ldx/.config/Typora/typora-user-images/image-20240401202336790.png)

## 2、div和span

```html
<div>
一个人占一整行。（块级标签）
</div>

<span>
自己多大占多少	。（行内标签）
</span>
```

![image-20240401202736370](/home/ldx/.config/Typora/typora-user-images/image-20240401202736370.png)

![image-20240401202809724](/home/ldx/.config/Typora/typora-user-images/image-20240401202809724.png)

## 3、超连接

```html
<a href="http://www.baidu.com">百度一下</a>
```

![image-20240401203854193](/home/ldx/.config/Typora/typora-user-images/image-20240401203854193.png)

## 4、图片

```html
<img src="图片地址" />
自己项目中创建static目录，图片要放在该目录中

设置图片的高宽
<img style="height: 300px" src="图片地址" />
```

![image-20240402083611931](../../../../../../home/ldx/.config/Typora/typora-user-images/image-20240402083611931.png)

## 5、列表

```html
无序列表
<ul>
    <li>中国移动</li>
    <li>中国电信</li>
    <li>中国联通</li>
</ul>
```

![image-20240402085120460](../../../../../../home/ldx/.config/Typora/typora-user-images/image-20240402085120460.png)

```html
有序列表
<ol>
    <li>中国移动</li>
    <li>中国电信</li>
    <li>中国联通</li>
</ol>
```

![image-20240402085156854](../../../../../../home/ldx/.config/Typora/typora-user-images/image-20240402085156854.png)

## 6、表格

```html
<table border="1"> # border边框
    <thead>
        # 表头	
        <tr>
            <th>ID</th>
            <th>姓名</th>
            <th>年龄</th>
        </tr>
    </thead>
    <tbody>
    	<tr>	
            <td>10</td>
            <td>ldx</td>
            <td>25</td>
        </tr>
        <tr>
            <td>11</td>
            <td>ldx</td>
            <td>25</td>
        </tr>
        <tr>
            <td>12</td>
            <td>ldx</td>
            <td>25</td>	</tr>
    </tbody>
    
</table>
```

![image-20240402090416690](../../../../../../home/ldx/.config/Typora/typora-user-images/image-20240402090416690.png)

## 7、input系列

```html
    <input type="text">
    <input type="password">
    <input type="file">
    
    <input type="radio" name = "n1">男    
    <input type="radio" name = "n1">女
    
    <input type="checkbox">篮球
    <input type="checkbox">足球
    <input type="checkbox">乒乓球

    <input type="button" value="提交"> 普通按钮
    <input type="submit" value="提交"> 提交表单
```

![image-20240402092108766](../../../../../../home/ldx/.config/Typora/typora-user-images/image-20240402092108766.png)

![image-20240402092212283](../../../../../../home/ldx/.config/Typora/typora-user-images/image-20240402092212283.png)

## 8、下拉框

```html
    <select>
        <option>北京</option>
        <option>上海</option>
        <option>深圳</option>
    </select>
```

![image-20240402095206864](../../../../../../home/ldx/.config/Typora/typora-user-images/image-20240402095206864.png)

## 9、多行文本

```html
<textarea rows="5"></textarea>
```

![image-20240402095734303](../../../../../../home/ldx/.config/Typora/typora-user-images/image-20240402095734303.png)

## 10、网络请求

* GET请求【URL方法、表单提交】
* POST请求 【表单提交】

