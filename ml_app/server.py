from flask import Flask,render_template,request
import numpy as np
import matplotlib.pyplot as plt
from predict_image import AI
my_app=Flask(_name_)
#MODEL_PATH='digit_AI'
MODEL_PATH='http://localhost:8501/v1/models/digit_GPT:predict'
ai=AI(MODEL_PATH)
@my_app.route('/',methods=['POST','GET'])
def home():
    return render_template('base.html',digit=prediction)
    @my_app.route('/predict',methods=['POST']
#     prediction=0
#     if request.method=='POST':
#         prediction=0
#         data=request.form.get('image')
#         data=np.fromstring(data,sep=',')
#         data=np.reshape(data,(500,500,-1))
#         prediction=ai(data[:,:,:3])
#         # plt.imshow(data[:,:,3])
#         # plt.show()
#         print(data.shape)
    
# @my_app.route('/page2')
# def page2():
#     return render_template('base.html')+'<font size=50>This is page 2</font>'

if _name=='__main__':
    my_app.run(debug=True)
