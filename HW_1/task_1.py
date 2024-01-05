"""
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна 
(шапка, меню, подвал), и дочерние шаблоны для страниц категорий 
товаров и отдельных товаров. Например, создать страницы 
«Одежда», «Обувь» и «Куртка», используя базовый шаблон.
"""


from flask import Flask, render_template, request, redirect, url_for, make_response


app = Flask(__name__)

# Базовый шаблон
@app.route('/')
def index():
    return render_template('index.html')

# Шаблон категории товаров
@app.route('/category/<category_name>')
def category(category_name):
    return render_template('category.html', category_name=category_name)

# Шаблон отдельного товара
@app.route('/product/<product_name>')
def product(product_name):
    return render_template('product.html', product_name=product_name)

@app.route('/category/<category_name>', methods=['GET', 'POST'])
def filtered_category(category_name):
    if request.method == 'POST':
        gender = request.form['gender']
        clothing_type = request.form['clothing_type']
        # Здесь вы можете использовать полученные значения для фильтрации товаров
        # и передать их в шаблон для отображения отфильтрованных товаров
        return render_template('filtered_category.html', category_name=category_name, gender=gender, clothing_type=clothing_type)

    return render_template('category.html', category_name=category_name)

if __name__ == '__main__':
    app.run(debug=True)



