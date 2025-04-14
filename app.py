from flask import Flask, render_template, request, redirect, url_for
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student = {
            "name": request.form['name'],
            "roll": request.form['roll'],
            "course": request.form['course'],
            "marks": request.form['marks']
        }
        blockchain.create_block(student)
        return redirect(url_for('view_chain'))
    return render_template('add_student.html')

@app.route('/chain')
def view_chain():
    chain = blockchain.get_chain()
    return render_template('view_chain.html', chain=chain)

if __name__ == '__main__':
    app.run(debug=True)
