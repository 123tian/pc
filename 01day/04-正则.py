import re

s = '''<!doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; chaRset=utf-8" />
<meta name="renderer" content="ie-stand">
<title>世说新语 - 内涵吧</title>
<meta name="applicable-device" content="pc">
<meta http-equiv="X-UA-Compatible" content="IE=9; IE=8; IE=7; IE=EDGE">
<meta name="keywords" content="" />
<meta name="description" content="让你了解最近网络上流行的语言都有什么，含义是什么，做一个用不out的人，就关注最新网络流行语吧，再不学习就真的out了！自造网络成语你懂吗？." />
<link rel="stylesheet" type="text/css" href="/css/wui_reset.css">
<link rel="stylesheet" type="text/css" href="/css/default.css">
<link rel="stylesheet" type="text/css" href="/css/css-shake.css">
<script src="/js/jquery-1.8.3.min.js"></script>
<script src="/js/jquery.timeago.js"></script>
<script src="/js/main.js"></script>
<link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.neihan8.com/lxy//" >
<script type="text/javascript">
(function(){var ua=navigator.userAgent.toLowerCase();var bIsIpad=ua.match(/ipad/i)=="ipad";var bIsIphoneOs=ua.match(/iphone os/i)=="iphone os";var bIsAndroid=ua.match(/android/i)=="android";var bIsWM=ua.match(/windows mobile/i)=="windows mobile";if(bIsIpad||bIsIphoneOs||bIsAndroid||bIsWM){window.location.href="http://m.neihan8.com/lxy//"}})();
</script>
</head>
<body>
<div class="wrap header">
  <div class="inner">
    <h2 class="logo"> <a href="/" ><img src="/images/logo.png" alt="内涵吧" /></a> </h2>
    <ul class="top-nav"><!--
      <li><a href="#" target="_blank" class="icon-hd-originality csshake shake-rotate">原创</a></li>
      <li><a href="#" target="_blank" class="icon-hd-bzp csshake shake-opacity">暴走拍</a></li>
      <li><a href="#" target="_blank" class="icon-hd-bqg csshake shake-rotate">表情馆</a></li>
      <li><a href="#" target="_blank" class="icon-hd-gg csshake shake-little">公告</a></li>
      <li><a href="#" target="_blank" class="icon-hd-xl csshake">系列</a></li>
      <li><a href="#" target="_blank" class="icon-hd-ncdh csshake shake-slow">脑残对话</a></li>
      <li><a href="#" target="_blank" class="icon-hd-gif csshake shake-hard">GIF怪兽</a></li>
      <li><a href="#" target="_blank" class="icon-hd-lt csshake shake-crazy">论坛</a></li>-->
      <li><a href="https://www.neihan8.com/tags/" target="_blank" class="icon-hd-stc csshake shake-rotate">神吐槽</a></li>
      <li><a href="/ribao/" target="_blank" class="icon-hd-bzrb csshake shake-opacity">内涵日报</a></li>
    </ul>
  </div>
</div>
<div class="wrap nav">
  <div class="inner">
    <div class="menu">
      <ul>
        <li class="home" id="nav-home"><a href="/" rel="nofollow">主站</a></li>
        <li class="menu-top" id="nav-pic"><a href="/tupian//"><img src="/images/pic-ico.png"/> 图片 <img src="/images/nav-arrow.png" /> </a>
          <ul class="menu-sub menu-text">           
           <li><a href="/pic//" title="内涵图">内涵图</a></li><li><a href="/mm/" title="妹纸图">妹纸图</a></li><li><a href="/ps/" title="恶搞PS">恶搞PS</a></li><li><a href="/pic/xlbk/" title="笑料百科">笑料百科</a></li><li><a href="/gaoxiaomanhua/" title="搞笑漫画">搞笑漫画</a></li><li><a href="/gif/" title="GIF动态图">GIF动态图</a></li><li><a href="/pic/mjx/" title="奇葩买家秀">奇葩买家秀</a></li><li><a href="/baozou/" title="暴走漫画">暴走漫画</a></li>  
          </ul>
        </li>
        <li class="menu-top"  id="nav-video"><a href="/shipin/"><img src="/images/video-ico.png"/> 视频 <img src="/images/nav-arrow.png" /> </a>
          <ul class="menu-sub menu-video " style="z-index: 999;">            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/" target="_blank"><img src="/images/video1.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/daomeixiong/" target="_blank"><img src="/images/video2.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/smzgw/" target="_blank"><img src="/images/video3.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/yqzsf/" target="_blank"><img src="/images/video4.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="#" target="_blank"><img src="/images/video5.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/laoshi/" target="_blank"><img src="/images/video6.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/mmhh/" target="_blank"><img src="/images/video7.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/jianbixiaohua/" target="_blank"><img src="/images/video8.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>           
          </ul>
        </li>
        <li class="menu-top" id="nav-txt"><a href="/wenzi//"><img src="/images/text-ico.png"/> 段子 <img src="/images/nav-arrow.png" /> </a>
        <ul class="menu-sub menu-text">
             <li><a href="/lxy//" title="世说新语">世说新语</a></li><li><a href="/lxh//" title="冷笑话">冷笑话</a></li><li><a href="/njjzw//" title="脑筋急转弯">脑筋急转弯</a></li><li><a href="/article//" title="内涵段子">内涵段子</a></li> 
          </ul>
        </li>
        <li><a href="/s/" target="_blank"><img src="/images/pb-ico.png"/> 瀑布流看图</a></li>
        <li><a href="/zm/" target="_blank"><img src="/images/zzq-ico.png"/>内涵字幕制作器</a></li>
      </ul>
    </div>
    <div class="user" id="show_userinfo"><li class="menu-pm"><a  href="javascript:void(0);" target="_self" onclick="AjaxLog()" rel="nofollow">登录</a></li><li class="menu-pm"><a href="/e/member/register/index.php?tobind=0&groupid=1" target="_blank" class="new_top_reg" rel="nofollow">注册</a></li></div>
  </div>
</div>
 <script type="text/javascript" src="/e/member/ajaxlog/?loadjs=1"></script>
<script>$("#nav-txt").addClass("curr");</script>
<div class="crumbs wrap">
<div class="inner">
<a href="/">内涵吧</a>&nbsp;>&nbsp;<a href="/wenzi//">段子</a>&nbsp;>&nbsp;<a href="/lxy//">世说新语</a>
</div>
</div><div class="main wrap">
  <div class="inner">
    <div class="left">
      <div class="column-title box box-790"> <a href="/lxy/" class="pic"> <img src="http://imgs.isocialkey.com/p/2015-09-23/cf0f9dc133cc2844f7bdb052034f5cb6.jpg" width="145" height="145" /> </a>
        <h1><a class="title">世说新语</a><b>作者：世说新语作者</b></h1>
        <div class="desc"> 让你了解最近网络上流行的语言都有什么，含义是什么，做一个用不out的人，就关注最新网络流行语吧，再不学习就真的out了！自造网络成语你懂吗？....</div>
      </div>      
      <div class="text-column-list mt10">      
           
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/148997.html" class="title" title="辣眼睛是什么意思">辣眼睛是什么意思</a></h3>
        <div class="desc">原本的意思就是指的辣椒水辣了眼睛，后来被网络小伙伴们采用之后，一般是指的被一个人的某些行为给恶心到了，不忍直视，比如微博现在特别火的蛇精男刘梓晨，大家就会经常说他辣眼睛。</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-08-16.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >2</div>
                <div class="bad" >0</div>
                <div class="view" >308</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/102019.html" class="title" title="友谊的小船说翻就翻是什么梗">友谊的小船说翻就翻是什么梗</a></h3>
        <div class="desc"> 　　观众朋友们，最近是不是与朋友稍有不和，友谊的小船说翻就翻了？讲真，我几乎每天都能在朋友圈和微博上见到这句话，看来大家心目中都驻着一搜“友谊号”。为了防止大家友谊之船</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-04-14.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >12</div>
                <div class="bad" >3</div>
                <div class="view" >1627</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/89221.html" class="title" title="打豆豆是什么意思">打豆豆是什么意思</a></h3>
        <div class="desc">　　一记者去南极采访众企鹅：“你们每天都做什么啊?”　　企鹅甲：“吃饭，睡觉，打豆豆。”　　企鹅乙：“吃饭，睡觉，打豆豆。”　　企鹅丙：“吃饭，睡觉，打豆豆。”　　&amp;hellip;&amp;hellip;</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-03-15.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >8</div>
                <div class="bad" >4</div>
                <div class="view" >1085</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/73741.html" class="title" title="笑哭是什么意思">笑哭是什么意思</a></h3>
        <div class="desc"> 　　2015年最火爆网络新词“笑哭”是什么意思？　　《牛津词典》宣布，《牛津词典》宣布，2015年的年度词汇是“笑cry”表情，没错，就是那个一边大笑，一边流眼泪的小黄脸。　　《牛津</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-01-13.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >19</div>
                <div class="bad" >6</div>
                <div class="view" >10788</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/73737.html" class="title" title="床咚是什么意思">床咚是什么意思</a></h3>
        <div class="desc"> 　　床咚，网络新词，形容把对方推倒在床上发出的声音。意指将对方强行按到床上示爱。　　详细释义：　　“床咚”是“壁咚”的衍生词。　　“壁咚”是日本流行词语，时常出现在少</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-01-13.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >22</div>
                <div class="bad" >9</div>
                <div class="view" >8967</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/68942.html" class="title" title="你咋不上天呢是个什么梗">你咋不上天呢是个什么梗</a></h3>
        <div class="desc"> 　　同学们好~今天老师要给大家科普的是最近常常在网络上见到的那句话&quot;你咋不上天呐&quot;是个什么梗　　东北的娃儿可以去操场玩了，造这是你妈从小教训你的必备语句...　　其他</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-12-16.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >48</div>
                <div class="bad" >10</div>
                <div class="view" >73041</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/67891.html" class="title" title="2015年的这些流行词，告诉你一个不一样的日本">2015年的这些流行词，告诉你一个不一样的日本</a></h3>
        <div class="desc"> 　　2015 年日本流行词评选的候选词汇出炉。从几个词看出一个国家的变化是很有意思的事情。　　1.爆买（爆買い）　　作为日本最有影响力的流行语榜单，《现代用语的基础知识》选</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-12-08.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >15</div>
                <div class="bad" >11</div>
                <div class="view" >2716</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/67725.html" class="title" title="主要看气质是什么梗">主要看气质是什么梗</a></h3>
        <div class="desc"> 　　最近，朋友圈都在晒“主要看气质”。　　很多人一边问：这是什么梗儿，一边也重复着同样的动作，贴上自己的自拍照片，然后打出：主要看气质。　　有的人考证说，这是一个恶搞游戏：　</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-12-07.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >20</div>
                <div class="bad" >5</div>
                <div class="view" >2367</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/65565.html" class="title" title="龙傲天是什么意思">龙傲天是什么意思</a></h3>
        <div class="desc"> 　　龙傲天，网络用语，多用于讽刺一些小说或动画，漫画中的主角。因为其人物特质和形象相反，以及作品内涵和作者写作功力较低所创造出来的一种饱受诟病的角色。　　“龙傲天”现</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-11-19.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >12</div>
                <div class="bad" >5</div>
                <div class="view" >1911</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/65564.html" class="title" title="强推是什么意思">强推是什么意思</a></h3>
        <div class="desc"> 　　强推，网络新词，是“强行推倒”的意思。　　详细释义：　　“强推”是“推倒”的引申，指由于动作者按捺不住自己强烈的欲望而对被动者实施强行推倒的动作。　　据统计，有过推</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-11-19.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >19</div>
                <div class="bad" >7</div>
                <div class="view" >5893</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/65563.html" class="title" title="B站是什么意思">B站是什么意思</a></h3>
        <div class="desc"> 　　B站，网络新词，一般指ACG弹幕分享网站bilibili（哔哩哔哩视频网）。　　B站由原AcFun网友“bishi”于2009年6月26日创建。由于AcFun网站在运行时往往不稳定，所以Mikufans建站的</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-11-19.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >21</div>
                <div class="bad" >9</div>
                <div class="view" >8644</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/65562.html" class="title" title="儿砸是什么意思">儿砸是什么意思</a></h3>
        <div class="desc"> 　　儿砸，网络新词，是“儿子”的意思。　　有很多地方的方言中，老爸喊自己的儿子的时候就是叫“儿砸”，当然，一般都是老爸比较高兴的时候。　　比如你考了一百分，老爸就会喊你，“</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-11-19.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >17</div>
                <div class="bad" >12</div>
                <div class="view" >6675</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/65561.html" class="title" title="帅帅哒是什么意思">帅帅哒是什么意思</a></h3>
        <div class="desc"> 　　帅帅哒，网络新词，是“帅帅的”比较萌的叫法。　　帅帅哒，意思就是很帅很帅，英俊潇洒，非常漂亮。　　例句：　　1、我哥帅帅哒，一直都是我崇拜的偶像。　　2、我男朋友长的帅帅</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-11-19.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >12</div>
                <div class="bad" >10</div>
                <div class="view" >1644</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/64360.html" class="title" title="甜文是什么意思">甜文是什么意思</a></h3>
        <div class="desc"> 　　甜文，网络新词，指文风甜蜜的文章，文章基调就是甜蜜，一般都是完美结局。　　“甜文”一般用来指喜剧小说，内容温馨甜蜜，大多会有幸福圆满的结局。　　甜文小说：　　《贵女长嬴</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-11-11.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >9</div>
                <div class="bad" >7</div>
                <div class="view" >1487</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/64359.html" class="title" title="虐文是什么意思">虐文是什么意思</a></h3>
        <div class="desc"> 　　虐文，网络新词，一般指虐待读者，或者虐待主角的小说。　　虐文分类：　　1、虐主角　　虐文小说，包括虐身和虐心，虐身主要是主角的身体被人虐待如SM文，或主角身患重病，无药可治。</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-11-11.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >10</div>
                <div class="bad" >3</div>
                <div class="view" >835</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/64357.html" class="title" title="小说爽文是什么意思">小说爽文是什么意思</a></h3>
        <div class="desc"> 　　爽文，网络新词，指看着让人很爽的小说。　　“爽文”大多指小说类型，一般“爽文”类小说情节的主人公都是顺风顺水，要什么就有什么。　　“爽文”主角想要钱，马上就中万百万；</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-11-11.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >13</div>
                <div class="bad" >9</div>
                <div class="view" >3184</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/64356.html" class="title" title="种田文是什么意思">种田文是什么意思</a></h3>
        <div class="desc"> 　　种田文，又称家常里短文，一般指以古代封建社会为背景的，或近现代科技不发达时期，描写小人物的家长里短，平淡生活琐事，更注重突出细节及人物心理描写。　　出处：　　“种田”一</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-11-11.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >10</div>
                <div class="bad" >6</div>
                <div class="view" >885</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/64354.html" class="title" title="高干文是什么意思">高干文是什么意思</a></h3>
        <div class="desc"> 　　高干文，网络新词，一般指以高级干部子女为主人公的小说类型。　　高干文是最近这几年在都市言情兴起的一种小说，主人公往往是社会高干的子弟孩子，描述了他们人生中所遇到的</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-11-11.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >5</div>
                <div class="bad" >3</div>
                <div class="view" >762</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/64352.html" class="title" title="小白文是什么意思">小白文是什么意思</a></h3>
        <div class="desc"> 　　小白文，网络新词，一般用来形容小说。　　小白文有如下三种意思：　　第一种，是指文采较次的文章，其文笔比较通俗，但却非常容易受到读者欢迎。说好听叫简单易懂，说难听点叫肤浅，</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-11-11.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >7</div>
                <div class="bad" >3</div>
                <div class="view" >902</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/64350.html" class="title" title="神烦是什么意思">神烦是什么意思</a></h3>
        <div class="desc"> 　　神烦，网络新词，是超级烦人的意思。　　“神烦”比“烦人”更高一个级别，“神烦”不是“烦恼”的意思哦。　　例句：　　1、我项链两千多，100块钱都不给我，我跟你有什么仇什么</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2015-11-11.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >13</div>
                <div class="bad" >3</div>
                <div class="view" >5111</div>             
            </div>
      </div>
	
      </div>     
       <div class="pagenav"><a href="/lxy//index.html">首页</a><a href="/lxy//index.html" class="prev">上一页</a><a href="/lxy//index.html">1</a><b>2</b><a href="/lxy//index_3.html">3</a><a href="/lxy//index_4.html">4</a><a href="/lxy//index_5.html">5</a><a href="/lxy//index_16.html">…</a><a href="/lxy//index_3.html" class="next">下一页</a><a href="/lxy//index_16.html">尾页</a><span>316条记录 2 / 16 页</span>
</div>
    </div>
<div class="sidebar">
  <div class="side-column side box">
    <h2 class="box-title" >
      <a class="name" href="/lxy/">世说新语</a>
    </h2>
    <div class="con">
	<a href="/lxy//" title="世说新语" id="cid12">世说新语</a><a href="/lxh//" title="冷笑话" id="cid13">冷笑话</a><a href="/njjzw//" title="脑筋急转弯" id="cid14">脑筋急转弯</a><a href="/article//" title="内涵段子" id="cid11">内涵段子</a>   
    </div>
  </div>
  <script type="text/javascript">
$("#cid12").addClass("curr");
</script>
  <div class="side-rank-tab side box">
    <h2 class="box-title" id="tabs">
      <li><a name="#con1">今日排行</a></li>
      <li><a name="#con2">本月排行</a></li>
      <li><a name="#con3">年度排行</a></li>
    </h2>
    <div class="con" id="cons">
      <div class="rank-list" id="con1">
        <ul>
		           <li>
            <div class="ico no-1">1</div>
            <a href="/av/34465.html" title="大桥未久(大橋未久)出道至今的作品封面以及番号大全">大桥未久(大橋未久)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-2">2</div>
            <a href="/av/34226.html" title="麻生希(あそうのぞみ)出道至今的作品封面以及番号大全">麻生希(あそうのぞみ)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-3">3</div>
            <a href="/gif/104028.html" title="真人做动态进出图片:男女配交图片100张 美国人拍的命根叉进女人">真人做动态进出图片:男女配交图片100张 美国人拍的命根叉进女人</a>
			</li>
                    <li>
            <div class="ico no-4">4</div>
            <a href="/av/34372.html" title="波多野结衣作品封面图片 はたの ゆい番号大全 波多野结衣家庭教师">波多野结衣作品封面图片 はたの ゆい番号大全 波多野结衣家庭教师</a>
			</li>
                    <li>
            <div class="ico no-5">5</div>
            <a href="/av/34300.html" title="京香Julia(julia)出道至今的作品封面以及番号大全">京香Julia(julia)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-6">6</div>
            <a href="/gif/197146.html" title="日本美女啪啪啪入室 站立背后入啪啪啪图片">日本美女啪啪啪入室 站立背后入啪啪啪图片</a>
			</li>
                    <li>
            <div class="ico no-7">7</div>
            <a href="/av/34475.html" title="濑亚美莉(一ノ瀬アメリ)出道至今的作品封面以及番号大全">濑亚美莉(一ノ瀬アメリ)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-8">8</div>
            <a href="/av/38002.html" title="新宅男AV女优林由奈出道至今作品番号封面 林ゆな番号大全">新宅男AV女优林由奈出道至今作品番号封面 林ゆな番号大全</a>
			</li>
                    <li>
            <div class="ico no-9">9</div>
            <a href="/av/34477.html" title="吉泽明步出道至今封面番号作品">吉泽明步出道至今封面番号作品</a>
			</li>
                    <li>
            <div class="ico no-10">10</div>
            <a href="/baozou/62656.html" title="厕所中的成语">厕所中的成语</a>
			</li>
                  </ul>
      </div>
      <div class="rank-list" id="con2">
        <ul>
                    <li>
            <div class="ico no-1">1</div>
            <a href="/av/34465.html" title="大桥未久(大橋未久)出道至今的作品封面以及番号大全">大桥未久(大橋未久)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-2">2</div>
            <a href="/av/34226.html" title="麻生希(あそうのぞみ)出道至今的作品封面以及番号大全">麻生希(あそうのぞみ)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-3">3</div>
            <a href="/gif/104028.html" title="真人做动态进出图片:男女配交图片100张 美国人拍的命根叉进女人">真人做动态进出图片:男女配交图片100张 美国人拍的命根叉进女人</a>
			</li>
                    <li>
            <div class="ico no-4">4</div>
            <a href="/av/34372.html" title="波多野结衣作品封面图片 はたの ゆい番号大全 波多野结衣家庭教师">波多野结衣作品封面图片 はたの ゆい番号大全 波多野结衣家庭教师</a>
			</li>
                    <li>
            <div class="ico no-5">5</div>
            <a href="/av/34300.html" title="京香Julia(julia)出道至今的作品封面以及番号大全">京香Julia(julia)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-6">6</div>
            <a href="/gif/197146.html" title="日本美女啪啪啪入室 站立背后入啪啪啪图片">日本美女啪啪啪入室 站立背后入啪啪啪图片</a>
			</li>
                    <li>
            <div class="ico no-7">7</div>
            <a href="/av/34475.html" title="濑亚美莉(一ノ瀬アメリ)出道至今的作品封面以及番号大全">濑亚美莉(一ノ瀬アメリ)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-8">8</div>
            <a href="/av/38002.html" title="新宅男AV女优林由奈出道至今作品番号封面 林ゆな番号大全">新宅男AV女优林由奈出道至今作品番号封面 林ゆな番号大全</a>
			</li>
                    <li>
            <div class="ico no-9">9</div>
            <a href="/av/34477.html" title="吉泽明步出道至今封面番号作品">吉泽明步出道至今封面番号作品</a>
			</li>
                    <li>
            <div class="ico no-10">10</div>
            <a href="/baozou/62656.html" title="厕所中的成语">厕所中的成语</a>
			</li>
                  </ul>
      </div>
      <div class="rank-list" id="con3">
        <ul>
                    <li>
            <div class="ico no-1">1</div>
            <a href="/av/34465.html" title="大桥未久(大橋未久)出道至今的作品封面以及番号大全">大桥未久(大橋未久)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-2">2</div>
            <a href="/av/34226.html" title="麻生希(あそうのぞみ)出道至今的作品封面以及番号大全">麻生希(あそうのぞみ)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-3">3</div>
            <a href="/gif/104028.html" title="真人做动态进出图片:男女配交图片100张 美国人拍的命根叉进女人">真人做动态进出图片:男女配交图片100张 美国人拍的命根叉进女人</a>
			</li>
                    <li>
            <div class="ico no-4">4</div>
            <a href="/av/34372.html" title="波多野结衣作品封面图片 はたの ゆい番号大全 波多野结衣家庭教师">波多野结衣作品封面图片 はたの ゆい番号大全 波多野结衣家庭教师</a>
			</li>
                    <li>
            <div class="ico no-5">5</div>
            <a href="/av/34300.html" title="京香Julia(julia)出道至今的作品封面以及番号大全">京香Julia(julia)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-6">6</div>
            <a href="/gif/197146.html" title="日本美女啪啪啪入室 站立背后入啪啪啪图片">日本美女啪啪啪入室 站立背后入啪啪啪图片</a>
			</li>
                    <li>
            <div class="ico no-7">7</div>
            <a href="/av/34475.html" title="濑亚美莉(一ノ瀬アメリ)出道至今的作品封面以及番号大全">濑亚美莉(一ノ瀬アメリ)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-8">8</div>
            <a href="/av/38002.html" title="新宅男AV女优林由奈出道至今作品番号封面 林ゆな番号大全">新宅男AV女优林由奈出道至今作品番号封面 林ゆな番号大全</a>
			</li>
                    <li>
            <div class="ico no-9">9</div>
            <a href="/av/34477.html" title="吉泽明步出道至今封面番号作品">吉泽明步出道至今封面番号作品</a>
			</li>
                    <li>
            <div class="ico no-10">10</div>
            <a href="/baozou/62656.html" title="厕所中的成语">厕所中的成语</a>
			</li>
                  </ul>
      </div>
    </div>
   <script src="/js/Tab.js"></script>
  </div>
   <div class="ad">
   </div>
  <div class="side-rank side box">
    <h2 class="box-title" >
      <a class="name" href="javascript:void(0);">世说新语好评榜</a>
      <a class="more" href="javascript:void(0);" rel="nofollow">更多+</a>
    </h2>
    <div class="con" >
      <div class="rank-list">
        <ul>
    <li>
      <div class="ico no-1">1</div>
            <a href="/lxy/68942.html" title="你咋不上天呢是个什么梗">你咋不上天呢是个什么梗</a></li>
		<li>
      <div class="ico no-2">2</div>
            <a href="/lxy/41493.html" title="sp主是什么意思">sp主是什么意思</a></li>
		<li>
      <div class="ico no-3">3</div>
            <a href="/lxy/156175.html" title="我和我大表哥二表哥都笑了">我和我大表哥二表哥都笑了</a></li>
		<li>
      <div class="ico no-4">4</div>
            <a href="/lxy/73737.html" title="床咚是什么意思">床咚是什么意思</a></li>
		<li>
      <div class="ico no-5">5</div>
            <a href="/lxy/157898.html" title=""蓝瘦香菇"是什么？">"蓝瘦香菇"是什么？</a></li>
		<li>
      <div class="ico no-6">6</div>
            <a href="/lxy/65563.html" title="B站是什么意思">B站是什么意思</a></li>
		<li>
      <div class="ico no-7">7</div>
            <a href="/lxy/67725.html" title="主要看气质是什么梗">主要看气质是什么梗</a></li>
		<li>
      <div class="ico no-8">8</div>
            <a href="/lxy/152166.html" title="当红炸子鸡是什么意思">当红炸子鸡是什么意思</a></li>
		<li>
      <div class="ico no-9">9</div>
            <a href="/lxy/65564.html" title="强推是什么意思">强推是什么意思</a></li>
		<li>
      <div class="ico no-10">10</div>
            <a href="/lxy/73741.html" title="笑哭是什么意思">笑哭是什么意思</a></li>
		        </ul>
      </div>
    </div>
  </div>
  <div class="scroll">
  <div class="side-tags side box">
    <h2 class="box-title"><a class="name" href="/tags/">热门标签</a><a class="more" href="/tags/" rel="nofollow">更多+</a></h2>
    <div class="con"> 
       <a target="_blank" href="http://www.neihan8.com/tags/hhhbl/" >很黄很暴力</a><a target="_blank" href="http://www.neihan8.com/tags/budejie/" >百思不得姐</a><a target="_blank" href="http://www.neihan8.com/tags/eblw/" >隔壁老王</a><a target="_blank" href="http://www.neihan8.com/tags/yeliangchen/" >叶良辰</a><a href="/tags/nvyou/" >女优</a><a href="/tags/meizi/" >妹纸</a><a href="/tags/laoshi/" >老师</a><a href="/tags/fuli/" >福利</a><a href="/tags/fuqi/" >夫妻</a><a href="/tags/2b/" >二逼</a><a href="/tags/nvshen/" >女神</a><a href="/tags/xiaoming/" >小明</a><a href="/tags/nvdiaosi/" >女吊丝</a><a href="/tags/mengchong/" >萌宠</a><a href="/tags/danshengou/" >单身狗</a><a href="/tags/tuhao/" >土豪</a><a href="/tags/xegif/" >邪恶动态图</a><a href="/tags/tongshi/" >同事</a><a href="/tags/xuduba/" >胥渡吧</a><a href="/tags/papapa/" >啪啪啪</a><a href="/tags/qigai/" >乞丐</a><a href="/tags/yisheng/" >医生</a><a href="/tags/tongzhuo/" >同桌</a>

     </div>
  </div>
     <div class="ad">
	 </div>
  </div>
    </div>
	</div>
</div>
   	  <script type="text/javascript" src="/js/scroll.js"></script>	
<script src='/e/public/onclick/?enews=doclass&classid=12'></script>
<div class="footer wrap">
<div class="inner">
    <div class="footer-block">
      <h4>关于我们</h4>
      <ul class="footer-ul">
        <li><a href="/about.html" target="_blank" rel="nofollow">网站简介</a></li>
        <li><a href="/duty.html" target="_blank" rel="nofollow">免责声明</a></li>
        <li><a href="/joinus.html" target="_blank" rel="nofollow">加入我们</a></li>
        <li><a href="/contact.html" target="_blank" rel="nofollow">联系我们</a></li>        
        <li><a href="/feedback.html" target="_blank" rel="nofollow">反馈意见</a></li>

      </ul>
    </div>
    <div class="footer-block">
      <h4>互动规则</h4>
      <ul class="footer-ul">
        <li><a href="#" target="_blank" rel="nofollow">投稿规则</a></li>
        <li><a href="#" target="_blank" rel="nofollow">审稿规则</a></li>
        <li><a href="#" target="_blank" rel="nofollow">升级规则</a></li>
      </ul>
    </div>    
    <div class="footer-block">
      <h4>关注我们</h4>
      <ul class="footer-ul">
        <li><a href="https://weibo.com/neihan8" target="_blank">新浪微博</a></li>
        <li><a href="https://weibo.com/neihan8" target="_blank">腾讯微博</a></li>
        <li><a href="https://tieba.baidu.com/f?kw=%E5%86%85%E6%B6%B5&ie=utf-8" target="_blank" rel="nofollow">百度贴吧</a></li>
        <li><a href="https://zhan.renren.com/neihan8com" target="_blank" rel="nofollow">人人小站</a></li>
        <li><a href="#" target="_blank" rel="nofollow">人人主页</a></li>
        <li><a href="#" target="_blank" rel="nofollow">新浪微刊</a></li>
      </ul>
    </div>
    <div class="footer-block">
<h4>内涵吧IOS版</h4>
<div class="qrcode"><img style="width: 120px; height: 120px;" src="/images/app_ios.jpg" alt="内涵吧IOS版" data-bd-imgshare-binded="1"></div>
</div>
<div class="footer-block">
<h4>内涵吧安卓版</h4>
<div class="qrcode"><img style="width: 120px; height: 120px;" src="/images/app_az.jpg" alt="内涵吧安卓版" data-bd-imgshare-binded="1"></div>
</div>
<div class="footer-sign">
    </div>
    <div class="cl">
        <p>Copyright 2005-2015 Neihan8.com <a href="/" target="_blank" title="内涵吧">内涵吧</a> 版权所有 <span style="color: #333333; font-size: 12px; line-height: 16px;">沪ICP备14040517号-1</span> <div style="display:none;"><script language="javascript" src="/js/stats.js"></script></div>
</p>
    </div>
</div>
</div>
<!--<a rel="nofollow" class="feedback">
反<br>馈</a> -->
<div class="backToTop"></div>
</body>
</html>'''

pattern = re.compile(r'.*?<div class="desc">(.*?)</div>',re.S)
result = re.findall(pattern,s)
print(result)