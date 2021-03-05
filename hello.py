from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/find_symbols_in_names', methods=["POST"])
def hello_world():
	request_data=request.get_json();
	a=request_data["chemicals"];
	b=request_data["symbols"];
	lis=[];
	for chemical in a:
		for symbol in b:
			if chemical.find(symbol)!=-1:
				lis.append(chemical.replace(symbol,"[{}]".format(symbol)))
	return jsonify({"result":", ".join(lis)})
        

  