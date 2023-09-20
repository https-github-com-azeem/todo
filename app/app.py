from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def message():  
      return render_template('index.html')  
      
     # return "Hi"
if __name__ == '__main__':  
   app.run(debug = False)  

   