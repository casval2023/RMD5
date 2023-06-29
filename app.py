

import streamlit as st

# 問題と解答のデータ
data = {
    "問1": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。不規則な食事（食事抜き、まとめ食い、深夜の飲食、早食い）は（　A　）をため込みます。不規則になった食事により、身体に（　B　）状態が生じ、常に（　C　）運動を起こすようになるからです。",
        "options": ["①疲れ", "②体脂肪", "③飢餓","④トランス","⑤レジスタンス","⑥リバウンド"],
        "answers": ["②体脂肪", "③飢餓","⑥リバウンド"]
    },
    "問2":{
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。私たちのからだは、交感神経と副交感神経という２つの（　A　）神経が備わっており、この二つがシーソーのように緊張と休息を交互に身体に与え（　B　）を維持しています。交感神経と副交感神経のカロリー摂取率は（　C　）倍も違うという事がわかっています。",
        "options": ["①自律", "②健康", "③体重", "④体脂肪", "⑤15〜20", "⑥20〜30"],
        "answers": ["①自律", "②健康", "⑤15〜20"
    },
    "問3": {
        "question": "Aにあてはまる言葉を下記①～③から１つ選び、文章を完成させましょう。食欲は、満腹中枢と摂食中枢でコントロールされており、食べ物が入り消化吸収されると、血液中にブドウ糖が増え、血糖と（　A　）の濃度が上がります。すると満腹中枢が刺激されて「もう満腹」と感じ、摂食中枢の活動が抑制されます。早食いの人はブレーキがかかる前にたくさん食べ、知らぬ間に食べ過ぎてしまう事になります。",
        "options": ["①インスリン", "②アドレナリン", "③コレステロール"],
        "answers": ["①インスリン"]
    },
    "問４": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。お酒を飲むと、肝臓はアルコールを分解するのに（　A　）をどんどん消費します。（　B　）が下がっていくと、今度は脳が空腹と勘違いして「食べろ」の指令を出してしまうのです。アルコールと、過剰摂取したおかずが（　C　）として体にたまってしまうので、お酒を飲むときのおかず（おつまみ）は低カロリー食品を心がけていただきたいものです。",
        "options": ["①たんぱく質", "②糖分", "③血糖値", "④血圧", "⑤脂質", "⑥中性脂肪"],
        "answers": ["②糖分", "③血糖値", "⑥中性脂肪"]
    } ,
    "問5": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。肥満には遺伝の要素があるとはいえ、体質だけではなく長い間につちかった（　A 　）の影響がとても大きいのです。ダイエットとは良い印象を与える（　B　）マナーを身に付けることと同じです。ちょっとした気持ちのいい（　C　）を生活に取り入れることができたら、ダイエットという意識でなくても太りにくい（　C　）を身に付けることにもなります。
",
        "options": ["①生活習慣", "②食習慣", "③ビジネス", "④テーブル", "⑤習慣", "⑥運動"],
        "answers": ["①生活習慣", "④テーブル", "⑤習慣"]
    }
}

def main():
    st.title('レギュラーダイエットマスター第5章復習問題')
    score = 0
    for key, value in data.items():
        st.write(f"### {key}")
        st.write(value["question"])
        answers = st.multiselect("選択肢を選んでください:", value["options"])
        if answers == value["answers"]:
            score += 1
            st.write("正解です！")
        #else:
            #st.write("不正解です。")
            #st.write(f"正解は {value['answers']} です。")
    st.write(f"### スコア: {score}/{len(data)}")
    st.write(f"# 正答率は **{round(score * 100/ len(data))}%** です！")

if __name__ == "__main__":
    main()
