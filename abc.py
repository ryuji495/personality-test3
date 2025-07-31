import streamlit as st

# 質問と選択肢の設定
question_tree = {
    "start": {"text": "あなたはよく外出をするほうですか？", "yes": "q1", "no": "q2"},
    "q1": {"text": "コミュ力があると思う？", "yes": "q3", "no": "q4"},
    "q2": {"text": "思考力があるほうだと思う？", "yes": "q4", "no": "q5"},
    "q3": {"text": "仲間が失敗しても許してあげる?", "yes": "q6", "no": "q7"},
    "q4": {"text": "自分は聞き上手だと思う？", "yes": "q8", "no": "q9"},
    "q5": {"text": "自分には特別な力があると思う", "yes": "j", "no": "i"},
    "q6": {"text": "自分より他人のことを優先する", "yes": "a", "no": "b"},
    "q7": {"text": "失敗してしまったら落ち込むよりもイライラする", "yes": "c", "no": "d"},
    "q8": {"text": "一人よりも大人数のほうがいい", "yes": "e", "no": "f"},
    "q9": {"text": "感情的になりやすいと思う？", "yes": "g", "no": "h"},
    "a": "🌟 あなたは **ポジティブタイプ** です！",
    "b": "🌸 あなたは **優しいタイプ** です！",
    "c": "🌧 あなたは **ネガティブタイプ** です！",
    "d": "🔥 あなたは **怒りっぽいタイプ** です！",
    "e": "❄️ あなたは **クールタイプ** です！",
    "f": "🌙 あなたは **おとなしいタイプ** です！",
    "g": "🎭 あなたは **感情豊かなタイプ** です！",
    "h": "💪 あなたは **熱血タイプ** です！",
    "i": "🌼 あなたは **天然タイプ** です！",
    "j": "🌀 あなたは **変人タイプ** です！"
}

# セッション状態を使って進行管理
if 'current_key' not in st.session_state:
    st.session_state.current_key = "start"

current_key = st.session_state.current_key

st.markdown("<h1 style='text-align: center;'>🧠 性格診断テスト</h1>", unsafe_allow_html=True)
st.markdown("---")

if current_key in question_tree and isinstance(question_tree[current_key], dict):
    question = question_tree[current_key]['text']
    with st.container():
        st.markdown(f"<div style='padding: 20px; border-radius: 10px; background-color: #f0f2f6;'><h3 style='text-align: center;'>{question}</h3></div>", unsafe_allow_html=True)
        
    st.markdown(" ")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("はい", use_container_width=True):
            next_key = question_tree[current_key]["yes"]
            st.session_state.current_key = next_key
            st.rerun()
        if st.button("いいえ", use_container_width=True):
            next_key = question_tree[current_key]["no"]
            st.session_state.current_key = next_key
            st.rerun()
else:
    st.success(question_tree[current_key])
    if st.button("もう一度やる"):
        st.session_state.current_key = "start"
        st.rerun()
