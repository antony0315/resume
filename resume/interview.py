import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt

image = Image.open('resume/0918988608-朱國安.jpg')
st.sidebar.title("朱國安的履歷")
st.sidebar.image(image,width=180)
st.sidebar.header("姓名:朱國安")
st.sidebar.header("生日:2000/03/15")
st.sidebar.header("畢業學校:逢甲大學")
st.sidebar.header("科系:財務工程與精算數學系")
st.sidebar.write('SKILL:統計、數據分析、python、R、SQL')
st.sidebar.write('興趣:投資、法律、心理學、程式語言')

st.sidebar.write("***")
st.sidebar.subheader(":telephone_receiver:連絡電話:0981064195")
st.sidebar.subheader(":email:Email:antony10283@gmail.com")




st.title('履歷')
st.subheader('關於我:')

path='resume/關於我.txt'
f = open(path, encoding="utf-8")
lines = f.readlines()
for line in lines:
    st.write(line)
f.close()



path3='resume/技能.txt'
f3 = open(path3, encoding="utf-8")
lines3 = f3.readlines()
with st.expander("程式技能"):
    for line3 in lines3:
        st.write(line3)
f.close()



df1 = pd.DataFrame(dict(
    score=[70,78,73,68,86,81,96,60,89,76],
    subjects=['會計學','體育','國文','經濟學', '創意思考 ','多元文化','APPS程式設計','大一英文','國防教育軍事訓練','公平交易法']))

df2 = pd.DataFrame(dict(
    score=[80,77,63,68,77,80,76,74,70,87],
    subjects=['體育','國文','經濟學','財務工程與精算導論', '公民參與 ','社會實踐','英文','大一英文','微積分','國防教育軍事訓練']))

df3 = pd.DataFrame(dict(
    score=[77,73,70,68,88,63,78,90],
    subjects=['精算定價模型','財務管理','財務資訊系統','保險學', '微積分 ','統計學','機率論','鑽石寶石及翡翠玉石之賞析鑑定']))

df4 = pd.DataFrame(dict(
    score=[80,77,75,80,64,91,90,92],
    subjects=['會計學','精算定價模型','財務數量方法','行銷管理', '統計學 ','綠色會計實作專題','資料搜索與探勘','財富管理']))

df5 = pd.DataFrame(dict(
    score=[60,80,77,75,60,84,99,78],
    subjects=['精算實務與軟體','衍生性金融商品','金融倫理','大三英文', '財務報表分析 ','數據分析軟體','期貨與選擇權','認識天然災害']))

df6 = pd.DataFrame(dict(
    score=[65,63,81,78,75,83,82,70,80,69],
    subjects=['精算實務與軟體','財務工程應用','管理學','行為經濟學','法律經濟學','證券交易法','生死與哲學','批判思考','王羲之手札賞析與臨摹','大陸問題研究']))

df7 = pd.DataFrame(dict(
    score=[90,86,66,90,91,65],
    subjects=['金融商品設計與開發','交易策略設計與分析','計量經濟學','民法概要','銀行授信管理','印尼語']))

df8 = pd.DataFrame(dict(
    score=[90,87,93,87,91],
    subjects=['精算大數據專題','金融APPS設計','投資策略實務','人工智慧導論','資料庫']))

fig1 = px.line_polar(df1, r='score', theta='subjects', line_close=True)
fig2 = px.line_polar(df2, r='score', theta='subjects', line_close=True)
fig3 = px.line_polar(df3, r='score', theta='subjects', line_close=True)
fig4 = px.line_polar(df4, r='score', theta='subjects', line_close=True)
fig5 = px.line_polar(df5, r='score', theta='subjects', line_close=True)
fig6 = px.line_polar(df6, r='score', theta='subjects', line_close=True)
fig7 = px.line_polar(df7, r='score', theta='subjects', line_close=True)
fig8 = px.line_polar(df8, r='score', theta='subjects', line_close=True)

st.subheader('學校成績')
option = st.selectbox('請選擇年級',('大一','大二','大三','大四'))
col1, col2= st.columns(2)
if option=='大一':
    with col1:
        st.subheader('上學期')
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.subheader('下學期')
        st.plotly_chart(fig2, use_container_width=True)
elif option=='大二':
    with col1:
        st.subheader('上學期')
        st.plotly_chart(fig3, use_container_width=True)
    with col2:
        st.subheader('下學期')
        st.plotly_chart(fig4, use_container_width=True)
elif option=='大三':
    with col1:
        st.subheader('上學期')
        st.plotly_chart(fig5, use_container_width=True)
    with col2:
        st.subheader('下學期')
        st.plotly_chart(fig6, use_container_width=True)
elif option=='大四':
    with col1:
        st.subheader('上學期')
        st.plotly_chart(fig7, use_container_width=True)
    with col2:
        st.subheader('下學期')
        st.plotly_chart(fig8, use_container_width=True)
st.subheader('我的作品集:')
skill = st.radio(
     "您要查看的作品集",
     ('python', 'R', 'SQL','其他'))


if skill=='python':
    program=st.selectbox('請選擇pythony作品:',('機器學習量化投資','加權指數與匯率關係','數據分析練習截圖','投資組合dashboard','蒙地卡羅模擬法','其他練習'))
elif skill=='R':
    program=st.selectbox('請選擇R練習作品:',('線性模型','資料前處理','模型'))
elif skill=='SQL':
    program=st.selectbox('請選擇SQL作品:',('SQL課程',))
elif skill=='其他':
    program=st.selectbox('請選擇其他作品:',('投資比賽','財報分析報告','multichart程式交易作業'))


if program=='機器學習量化投資':
    st.write('開發專案:利用機器學習分類方法，協助判斷股市多空行情，交叉驗證準確度88%，標準差1%')
    pdfFileObj = open('resume/基於機器學習模型對台灣加權指數量化交易研究.pdf', 'rb')
    st.download_button(
        label="Download 基於機器學習模型對台灣加權指數量化交易研究.pdf",
        data=pdfFileObj,
        file_name='基於機器學習模型對台灣加權指數量化交易研究.pdf',
        mime='pdf',
    )
    for i in range(15):
        i = Image.open('resume/1-{}.png'.format(i+1))
        st.image(i,width=800)

elif program=='加權指數與匯率關係':
    st.write(
        '''曾經聽到某位分析師說新台幣不停的升值，會造成公司匯損，股價會下跌，抱持著好奇心的我，透過回歸分析發現，與他所講的不同
        ，新台幣與股市為負向關係，且回歸R-square高達92%，也幫助我在四月份時發現台幣開始貶值，避開下跌段
        ''')
    for i in range(3):
        i = Image.open('resume/2-{}.png'.format(i+1))
        st.image(i,width=800)
elif program=='數據分析練習截圖':
    st.subheader('python數據分析練習:')
    st.text('''
    學習python統計各種方法，透過程式語言有:更快、速避免計算錯誤、不用硬背公式等優點，幫助我分析不同問題
    ''')
    st.image(Image.open('resume/3-1.png'),width=300)
    st.subheader('''分類方法:KNN、決策樹、RandomForest、SVM、LDA''')
    st.image(Image.open('resume/3-2.png'),width=800)
    st.subheader('''變異數分析ANOVA:一元變異數分析、多重比較檢驗、多因素分析、交互影響''')
    st.image(Image.open('resume/3-3.png'),width=800)
    st.subheader('''列連分析、對應分析MCA''')
    st.image(Image.open('resume/3-4.png'),width=800)
    st.subheader('相關分析、關聯分析:')
    st.image(Image.open('resume/3-5.png'),width=800)
    col1,col2=st.columns(2)
    with col1:
        st.subheader('假設檢定')
        st.image(Image.open('resume/3-6.png'),width=400)
    with col2:
        st.subheader('回歸分析')
        st.image(Image.open('resume/3-7.png'),width=400)
elif program=='投資組合dashboard':
    st.subheader('投資組合dashboard:')
    st.write('利用效率前緣理論，幫助投資人於台股前100大公司中，投資組合達到最佳投資組合資產配置')
    st.subheader('https://share.streamlit.io/antony0315/stockprofolio/main/dashboard.py')
    for i in range(3):
        i = Image.open('resume/4-{}.png'.format(i+1))
        st.image(i,width=800)
elif program=='蒙地卡羅模擬法':
    st.write('透過蒙地卡羅模擬法，尋找出股價波動的最大風險')
    for i in range(3):
        i = Image.open('resume/5-{}.png'.format(i+1))
        st.image(i,width=600)
elif program=='其他練習':
    st.subheader('logit回歸練習')
    st.image(Image.open('resume/6-1.png'),width=800)
    st.subheader('LSTM模型預測航空公司旅客人數')
    st.image(Image.open('resume/6-2.png'),width=800)
    st.subheader('tensorflow練習')
    st.image(Image.open('resume/6-3.png'),width=800)
    st.image(Image.open('resume/6-4.png'),width=800)
    st.subheader('selenium自動化爬蟲')
    st.video('resume/v1.mp4',"mp4")
    st.subheader('word2vec+RNN語意分析練習')
    st.image(Image.open('resume/6-5.png'),width=700)
    st.image(Image.open('resume/6-6.png'),width=700)
    st.image(Image.open('resume/6-7.png'),width=700)
    st.image(Image.open('resume/6-8.png'),width=700)


if program=='線性模型':
    st.write('線性模型')
    for i in range(6):
        i = Image.open('resume/2-1-{}.png'.format(i+1))
        st.image(i,width=800)
elif program=='資料前處理':
    st.write('資料前處理')
    st.subheader('outlier_test')
    st.image(Image.open('resume/2-2-1.png'),width=800)
    st.subheader('PCA降維')
    st.image(Image.open('resume/2-2-2.png'),width=800)
elif program=='模型':
    st.subheader('決策樹模型')
    st.image(Image.open('resume/2-3-1.png'),width=800)
    st.subheader('XGBOOST')
    st.image(Image.open('resume/2-3-2.png'),width=800)

if program=='SQL課程':
    st.subheader('SQL_sever_2019')
    st.image(Image.open('resume/3-1-1.png'),width=700)
    st.subheader('ER_model')
    st.image(Image.open('resume/3-1-2.png'),width=700)
    st.subheader('查詢語法')
    st.image(Image.open('resume/3-1-3.png'),width=700)
    st.subheader('進階查詢語法')
    st.image(Image.open('resume/3-1-4.png'),width=700)
    st.subheader('巢狀語法')
    st.image(Image.open('resume/3-1-5.png'),width=700)
    st.image(Image.open('resume/3-1-6.png'),width=700)
    st.subheader('python串接MS SQL')
    st.image(Image.open('3-1-7.png'),width=700)
    

if program=='投資比賽':
    st.write('參與了3次元大證券辦得投資競賽，兩次於數千人之中進入前1%，投資是一項有趣的活動，結合了對產業知識的了解，時事的分析，與各項數據的洞察，綜合各項資訊做出判斷')
    st.write('相關報導'+'https://www.chinatimes.com/newspapers/20201223000349-260206?chdtv')
    st.image(Image.open('resume/4-1-3.png'),width=700)
    col1,col2=st.columns(2)
    with col1:
        st.image(Image.open('resume/4-1-1.jpg'),width=300)
    with col2:
        st.image(Image.open('resume/4-1-2.jpg'),width=300)
    st.image(Image.open('resume/4-1-4.png'),width=800)
elif program=='財報分析報告':
    st.write('財報分析課程分析報告')
    pdfFileObj = open('resume/研究報告.pdf', 'rb')
    st.download_button(
        label="Download 研究報告.pdf",
        data=pdfFileObj,
        file_name='研究報告.pdf',
        mime='pdf',
    )
    pdfFileObj = open('resume/被動元件族群財務狀況比較.pdf', 'rb')
    st.download_button(
        label="Download 被動元件族群財務狀況比較.pdf",
        data=pdfFileObj,
        file_name='被動元件族群財務狀況比較.pdf',
        mime='pdf',
    )
elif program=='multichart程式交易作業':
    for i in range(3):
        i = Image.open('resume/5-1-{}.png'.format(i+1))
        st.image(i,width=600)
    st.image(Image.open('resume/5-1-5.jpg'),width=600)
