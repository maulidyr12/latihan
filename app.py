'''
	AIM4 - Flask - [A] Basic - [03] Template
	
	Orbit Future Academy - AI Mastery - KM Batch 4
	Tim Deployment
	2023
'''

# =[Modules dan Packages]========================
from flask import Flask,render_template
from flask_ngrok import run_with_ngrok

# =[Variabel Global]=============================
app = Flask(__name__, static_url_path='/static')

# =[Routing]=====================================
@app.route("/")
def beranda():
    return render_template('CVMR.html')

# =[Main]========================================
if __name__ == '__main__':
    run_with_ngrok(app)
    app.run()
