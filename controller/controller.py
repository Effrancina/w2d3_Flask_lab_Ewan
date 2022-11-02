from flask import render_template
from app import app
from models.order_list import orders

@app.route('/orders')
# def index(order_id):
#     return render_template('index.html', title="Home", orders=orders, order=orders[int(order_id)])
def index():
    return render_template('index.html', title="Home", orders=orders)

# @app.route('/order/any'.format(str(orders)[1:-1]))
@app.route('/orders/<order_id>')
def order(order_id):
    return render_template('order.html', title="Individual order", order=orders[int(order_id)])
    #  return render_template('order.html', title="Individual order", order=order)