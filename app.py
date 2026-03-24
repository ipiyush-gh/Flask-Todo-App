from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
    
    sorted_tasks = sorted(tasks, key=lambda x: priority_order.get(x['priority'], 4))
    
    return render_template('index.html', tasks=sorted_tasks)

@app.route('/add', methods=['POST'])
def add():
    text = request.form.get('task')
    priority = request.form.get('priority')
    category = request.form.get('category')

    if text:
        tasks.append({
            'text': text,
            'done': False,
            'priority': priority,
            'category': category
        })
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    if 0 <= id < len(tasks):
        tasks.pop(id)
    return redirect('/')

@app.route('/complete/<int:id>')
def complete(id):
    if 0 <= id < len(tasks):
        tasks[id]['done'] = not tasks[id]['done']
    return redirect('/')

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    new_text = request.form.get('new_task')
    if new_text and 0 <= id < len(tasks):
        tasks[id]['text'] = new_text
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)