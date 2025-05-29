from flask import Flask , request , jsonify

app = Flask(__name__)

#簡単なレシピ辞書(必要に応じて追加OK)
recipes = {
    "鹿のロースト": "鹿肉を塩胡椒でマリネし、180度のオーブンで15分焼きます。 ",
    "猪の味噌煮込み": "猪肉を下茹でし、味噌、酒、みりんでコトコト煮ます。 ",
    "鹿カレー ": "鹿肉を炒めて、玉ねぎ・カレー粉・スパイスで煮込んで完成！ ",
    "猪焼肉":"猪肉をスライスして焼き肉のタレに漬け込み、強火で焼くだけ！",
}

@app.route("/api/recipe", methods=["GET"])
def get_recipe():
    dish = request.args.get("dish")
    result = recipes.get(dish,"レシピが見つかりませんでした。")
    return jsonify({"result":result})
  
if __name__=="__main__":
    app.run(debug=True)