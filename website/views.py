from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/home')
def home():
    return render_template('home.html')

@views.route('/booking',methods=['GET','POST'])
@login_required
def booking():
    global lokasi
    if request.method == 'POST':
        lokasi = request.form.get('lokasi')
        return redirect(url_for('views.transaksi'))
    
    return render_template('booking.html')

@views.route('transaksi',methods=['GET','POST'])
@login_required
def transaksi():
    print(lokasi)
    return render_template('transaksi.html')

@views.route('/admin',methods=['GET','POST'])
@login_required
def admin():
    return render_template('admin.html')
