from flask import Flask, request, render_template
import palm as pl , markdown2 as ml,translate as tl


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # Get user input from the form
        
        
        user_input = request.form.get('user_input')

        
        try:
            processed_input = ml.markdown(pl.MCbot(user_input))
        except Exception as e:
        # Handle the exception, e.g., print an error message
            
            processed_input = "Error: Unable to process input"


        
        return render_template('index.html', processed_input=processed_input)

    
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def process_generated_text():
     if request.method=='POST' :
        generated_text=request.form.get('hidden_generated_text')
        selected_language=request.form.get('selected_languages')

        translated_content=tl.translate(generated_text,selected_language)
        

        return render_template('index.html',processed_input=translated_content)
        
     return render_template('index.html')
    
   


   





if __name__ == '__main__':
    app.run(debug=True)

