import streamlit as st
from  PIL import Image

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智能词典','我的留言区','真心话大冒险','作者的碎碎念'])

def page1():
    st.write(":sparkles:兴趣推荐页:sparkles:")
    tab1,tab2,tab3,tab4,tab5,tab6,tab7 = st.tabs(['简介','莲花楼','王权富贵','英雄志','沉香如屑','南风知我意','赴山海'])
    with tab1:
        st.write(":pretzel:兴趣：追剧")
        st.write(":pretzel:喜欢的演员：成毅")
        st.write(":pretzel:爱好：发呆")
        st.write(':pretzel:观影软件：')
        
        go = st.selectbox('选择想要查看的网页', ['爱奇艺','腾讯','芒果','优酷','bilibili'])
        if go == '爱奇艺':
            st.link_button('去'+go+'观影','https://www.iqiyi.com/' )
        elif go == '腾讯':
            st.link_button('去'+go+'观影','https://v.qq.com/channel/tv' )
        elif go == '芒果':
            st.link_button('去'+go+'观影','https://www.mgtv.com/' )
        elif go == '优酷':
            st.link_button('去'+go+'观影','https://www.youku.com/' )
        elif go == 'bilibili':
            st.link_button('去'+go+'观影','' )
            
        st.write("-------未完待续-------")
    with tab2:
        st.write(':ice_cream:莲花楼:ice_cream:')
        st.image('莲花楼.jpg')
        st.write('《莲花楼》改编自藤萍的小说《吉祥纹莲花楼》，讲述了闻名武林的四顾门门主李相夷在一次大战后身受重伤，从此退隐江湖成为淡泊名利的郎中李莲花，在遇到新交方多病与旧敌笛飞声后重新卷入江湖的故事。') 
    with tab3:
        st.write(':ice_cream:王权富贵:ice_cream:')
        st.image('王权富贵.jpg')
        st.write('该剧根据庹小新创作的漫画作品《狐妖小红娘》改编，讲述了自幼被当作一气盟斩妖除魔终极兵器培养的王权富贵，遇到了潜入王权山庄做间谍的蜘蛛精清瞳。清瞳的出现，越发激起富贵对妖怪看法的改变，也给富贵展示了更多外面的世界。富贵内心渴望自由、憧憬天下大同的信念被逐渐点燃，经历万剑穿心，带着清瞳离开王权山庄，走上了自己所悟之道。')
    with tab4:
        st.write(':ice_cream:英雄志:ice_cream:')
        st.image('英雄志.jpg')
        st.write('该剧讲述了以土木堡之变为背景，复辟斗争为舞台，故事生动地展现了英雄们与时代的交融与碰撞。卢云、伍定远、秦仲海和杨肃观，在江湖中并肩作战，共同面对各种考验与机缘。他们与一众风云人物一起，经历了跌宕起伏的命运，勇敢面对了爱与恨、情与仇的抉择，并最终达成了他们报效国家的崇高理想。')
    with tab5:
        st.write(':ice_cream:沉香如屑:ice_cream:')
        st.image('沉香如屑.jpg')
        st.write('该剧改编自苏寞的同名小说，讲述了菡萏仙子颜淡与六界帝君应渊联手向恶势力宣战，在相知相识中逐渐解开以往的误会，最终携手维护人间正道、共同守护天下苍生的曲折故事')
        

    with tab6:
        st.write(':ice_cream:南风知我意:ice_cream:')
        st.image('南风知我意.jpg')
        st.write('该剧根据七微的同名小说改编，讲述了为寻找天然药物的傅云深与前往欠发达地区进行医学调研的朱旧相遇后，开启的一段相爱相杀、相互治愈的恋爱故事')
        

    with tab7:
        st.write(':ice_cream:赴山海:ice_cream:')
        st.image('赴山海.jpg')
        st.write('该剧改编自温瑞安的小说《神州奇侠》，讲述了一名酷爱武侠小说却被现实磨平棱角的咸鱼肖明明，以小说男主角萧秋水的视角游历了一次武林世界，从武力低微、热血冲动的少年剑客，最终成长为有情有义、守护家国的大侠。此后肖明明在工作之余也不忘创作，在小说中继续传递人心因义而聚的信念的故事')
        
        
def page2():
    '''我的图片处理工具'''
    st.write(':sparkles:图片换色小程序:sparkles:')
    uploaded_file=st.file_uploader('图片上传',type=['png','jpeg','jpg'])
    if uploaded_file:
        tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(['原图','改色1','改色2','改色3','旋转90度','旋转180度'])
        img = Image.open(uploaded_file)
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,1,0,2))
        with tab3:
            st.image(img_change(img,0,2,1))
        with tab4:
            st.image(img_change(img,2,1,0))
        with tab5:
            st.image(img.rotate(90))
        with tab6:
            st.image(img.rotate(180))
        

def img_change(img,rc,gc,bc):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img

def page3():
    st.write(':sparkles:智慧词典:sparkles:')
    
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')

    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')

    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]

    
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')

    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')

    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])

    
    word =  st.text_input('请输入您想查询的单词:')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1

        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)


        st.write('单词的查寻次数为：',times_dict[n])
        

        if word == 'python':
            st.code('''
                    #恭喜你触发彩蛋
                    print('Hello,python')''')
        if word == 'jieziqing':
            st.snow()
            st.info('没想到吧，彩蛋就是我:poop::poop::poop:')
        if word == 'chengyi':
            st.balloons()
            st.info(':innocent::innocent::innocent:')
        


def page4():
    '''我的留言区'''
    st.write(':sparkles:留言区:sparkles:')
    # 读取留言文件
    try:
        with open('leave_messages.txt', 'r', encoding='utf-8') as f:
            # 读取文件内容并按行分割
            messages_list = f.read().split('\n')
        # 对每一行留言进行分割处理
        for i in range(len(messages_list)):
            messages_list[i] = messages_list[i].split('#') if messages_list[i] else []
    except FileNotFoundError:
        # 如果文件不存在，初始化空列表
        messages_list = []
    # 初始化消息列表到 session_state
    if 'messages_list' not in st.session_state:
        st.session_state.messages_list = messages_list
    # 显示历史消息
    for message in st.session_state.messages_list:
        # 确保留言至少有三个元素（序号、发送者、内容）
        if len(message) >= 3:
            sender = message[1]
            content = message[2]
            if sender == '果果':
                with st.chat_message('🌻'):
                    st.write(sender, ':', content)
            elif sender == '花花':
                with st.chat_message('🌸'):
                    st.write(sender, ':', content)
            elif sender == '小鱼':
                with st.chat_message('🐟'):
                    st.write(sender, ':', content)
            elif sender == '糖粥':
                with st.chat_message('🍛'):
                    st.write(sender, ':', content)
    # 用户选择名字和输入新消息
    name = st.selectbox('我是...', ['果果', '花花','小鱼','糖粥'])
    new_message = st.text_input('想要说的话:')
    # 处理用户点击留言按钮的操作
    if st.button('留言'):
        if new_message.strip():  # 检查输入是否不为空或仅包含空白字符
            # 为消息添加序号
            if st.session_state.messages_list:
                message_id = str(int(st.session_state.messages_list[-1][0]) + 1)
            else:
                message_id = '1'
            # 添加新消息到 session_state
            st.session_state.messages_list.append([message_id, name, new_message])
            try:
                # 将更新后的消息列表写入文件
                with open('leave_messages.txt', 'w', encoding='utf-8') as f:
                    # 使用列表推导式和 join 方法生成文件内容
                    message_content = '\n'.join(['#'.join(msg) for msg in st.session_state.messages_list])
                    f.write(message_content)
                # 清空输入框并刷新页面
                st.experimental_rerun()
            except Exception as e:
                # 若保存留言时出现错误，显示错误信息
                st.error(f"保存留言时出现错误: {e}")

def page5():
    st.write(':sparkles:真心话大冒险:sparkles:')
    
    st.write(':ice_cream:你最喜欢哪个角色？')
    cb1 = st.checkbox('花花')
    cb2 = st.checkbox('小鱼')
    cb3 = st.checkbox('翻龟君')
    cb4 = st.checkbox('芙芙')
    l = [cb1, cb2, cb3, cb4]
    if st.button('确认答案'):
        if cb1 == True :
            st.write('去去重去去，来时是来时。')
        elif cb2 == True:
            st.write('那高处我去过!')
        elif cb3 == True:
            st.write('我早已不在乎什么天规，若能跟心爱之人在一起，舍下这帝君之位又何妨？')
        elif cb4 == True:
            st.write('只要能活着出去，万水千山愿意陪我看吗？')

    st.write(':ice_cream:你是几代果果？')
    nb1 = st.checkbox('one')
    nb2 = st.checkbox('two')
    nb3 = st.checkbox('three')
    nb4 = st.checkbox('four')
    l2 = [nb1, nb2, nb3, nb4]
    if st.button('已选择'):
        if nb1 == True :
            st.write('有毅力，为你点赞!!!')
        elif nb2 == True:
            st.write('哇塞！！！')
        elif nb3 == True:
            st.write('要继续坚持哦~~~')
        elif nb4 == True:
            st.write('正处于热恋期呢~')

    st.write('-------未完待续-------')

def page6():
    st.write(':sparkles:作者的碎碎念:sparkles:')
    st.write(':sweet_potato:围脖：诗晴-17(看后续)')


if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智能词典':
    page3()
elif page == '我的留言区':
    page4()
elif page == '真心话大冒险':
    page5()
elif page == '作者的碎碎念':
    page6()