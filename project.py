from flask import Flask, request, render_template
app = Flask(__name__, template_folder="templates")

@app.route('/')
def first():
    return render_template('project.html')
    
@app.route('/answer')
def ans():
    query = request.args['query']
    method = request.args['method']
    answer = tf_idf_search(query)      
    return render_template('answer.html', query = query, method = method, answer = answer)
   
if __name__ == "__main__":
    app.run()
