import streamlit as st

def charger_styles_css():
    with open("style.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load your logo image
logo = "images/logo.jpg"
st.image(logo, width=150)
# Définition initiale de la liste des questions et réponses.
questions_reponses_initiales = [
   {"question": "Qu'indique le sujet dans une phrase ?", "answer": "Qui fait l'action."},
    {"question": "Comment trouve-t-on le sujet d'un verbe conjugué ?", "answer": "En posant la question « Qui ? » ou « Qu'est-ce qui ? » avant le verbe."},
    {"question": "Quel exemple montre comment trouver le sujet dans la phrase « Roméo s'approche de Juliette » ?", "answer": "Qui s'approche de Juliette ? Réponse : Roméo."},
    {"question": "De quoi le sujet commande-t-il l'accord dans une phrase ?", "answer": "Du verbe en personne et en nombre."},
    {"question": "Qu'arrive-t-il quand un verbe possède plusieurs sujets ?", "answer": "Il s'accorde au pluriel."},
    {"question": "Quel exemple illustre l'accord du verbe avec plusieurs sujets ?", "answer": "Le frère et la sœur entrent dans le magasin."},
    {"question": "Que devient le sujet quand il suit le verbe ?", "answer": "Un sujet inversé."},
    {"question": "Quelles peuvent être les classes grammaticales du sujet ?", "answer": "Un nom, un pronom, un verbe à l'infinitif, une proposition subordonnée."},
    {"question": "Que commande le sujet en termes d'accord ?", "answer": "L'accord du verbe en personne et en nombre."},
    {"question": "Un même sujet peut-il commander l'accord de combien de verbes ?", "answer": "Plusieurs."},
    {"question": "Quel exemple montre un sujet commandant l'accord de plusieurs verbes ?", "answer": "Roméo se cacha dans l'ombre, ferma les yeux et écouta Juliette."},
    {"question": "Que font les compléments essentiels dans une phrase ?", "answer": "Ils complètent un verbe et font partie du groupe verbal."},
    {"question": "Que se passe-t-il si on supprime un complément essentiel ?", "answer": "On change complètement le sens de la phrase."},
    {"question": "Quels sont les types de compléments essentiels ?", "answer": "Les compléments d'objet (COD et COI), l'attribut du sujet, et les compléments essentiels de lieu, de temps et de mesure."},
    {"question": "Qu'est-ce qui différencie un complément essentiel d'un complément de phrase ?", "answer": "Un complément essentiel ne peut ni être supprimé, ni déplacé sans changer le sens de la phrase."},
    {"question": "Comment trouve-t-on le COD dans une phrase ?", "answer": "En posant la question « Qui ? » ou « Quoi ? » après le verbe."},
    {"question": "Quelle est la construction grammaticale du COD par rapport au verbe ?", "answer": "De manière « directe » après le verbe."},
    {"question": "Quelles peuvent être les classes grammaticales du COD ?", "answer": "Un nom, un pronom. un groupe nominal (GN)"},
    {"question": "Quel exemple illustre un COD sous forme de verbe ou groupe verbal à l'infinitif ?", "answer": "« Il me demande de venir. »"},
    {"question": "Comment un COD peut-il être remplacé dans une phrase ?", "answer": "Par un pronom tel que le, la, les, en."},
    {"question": "Comment trouve-t-on le COI dans une phrase ?", "answer": "En posant la question « À qui ? », « À quoi ? » ou « De quoi ? » après le verbe."},
    {"question": "Quelle est la construction grammaticale du COI par rapport au verbe ?", "answer": "De manière « indirecte » après le verbe, avec une préposition avant le complément."},
    {"question": "Quelles peuvent être les classes grammaticales du COI ?", "answer": "un pronom,Un groupe prépositionnel"},
    {"question": "Donnez un exemple où le COI est remplacé par un pronom.", "answer": "« Nous lui obéissons. »"},
    {"question": "Par quels pronoms un COI peut-il être remplacé ?", "answer": "Par lui, leur, y, en."},
    {"question": "Qu'indique l'attribut du sujet dans une phrase ?", "answer": "Une caractéristique du sujet."},
    {"question": "Quels types de verbes sont utilisés avec l'attribut du sujet ?", "answer": "Des verbes d'état comme être, sembler, devenir."},
    {"question": "Donnez un exemple de verbe employé de manière attributive.", "answer": "« Il a été élu délégué de la classe. »"},
    {"question": "Quelles peuvent être les classes grammaticales de l'attribut du sujet ?", "answer": "Un adjectif, un nom,un pronom,GN, un verbe à l'infinitif."},
    {"question": "Donnez un exemple où l'attribut du sujet est une proposition subordonnée.", "answer": "« Le mieux est que tu viennes. »"}
]
# Initialisation de la session et des variables d'état si elles n'existent pas
def initialiser_session():
    if 'questions_reponses' not in st.session_state:
        st.session_state.questions_reponses = questions_reponses_initiales.copy()
    if 'index_actuel' not in st.session_state:
        st.session_state.index_actuel = 0
    if 'voir_reponse' not in st.session_state:
        st.session_state.voir_reponse = False
    if 'quitter' not in st.session_state:
        st.session_state.quitter = False

def afficher_question():
    index = st.session_state.index_actuel
    qr = st.session_state.questions_reponses[index]
    if not st.session_state.voir_reponse:
        st.markdown(f"<div class='card-question'><h4><span class='question-prefix'>Question {index + 1}:</span> {qr['question']}</h4></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='card-reponse'><h4><span class='answer-prefix'>Réponse {index + 1}:</span> {qr['answer']}</h4></div>", unsafe_allow_html=True)

def bouton_voir_reponse():
    st.session_state.voir_reponse = True

def bouton_cacher_reponse():
    st.session_state.voir_reponse = False

def bouton_precedent():
    st.session_state.index_actuel = (st.session_state.index_actuel - 1) % len(st.session_state.questions_reponses)
    bouton_cacher_reponse()

def bouton_suivant():
    st.session_state.index_actuel = (st.session_state.index_actuel + 1) % len(st.session_state.questions_reponses)
    bouton_cacher_reponse()

def bouton_jeter():
    if len(st.session_state.questions_reponses) > 1:
        del st.session_state.questions_reponses[st.session_state.index_actuel]
        st.session_state.index_actuel %= len(st.session_state.questions_reponses)
    else:
        st.error("Il doit rester au moins une question.")
    bouton_cacher_reponse()

def bouton_classer():
    if st.session_state.index_actuel < len(st.session_state.questions_reponses) - 1:
        question = st.session_state.questions_reponses.pop(st.session_state.index_actuel)
        insert_at = (st.session_state.index_actuel + 1) % len(st.session_state.questions_reponses)
        st.session_state.questions_reponses.insert(insert_at, question)
    bouton_cacher_reponse()

def recommencer():
    st.session_state.questions_reponses = questions_reponses_initiales.copy()
    st.session_state.index_actuel = 0
    bouton_cacher_reponse()
    st.session_state.quitter = False

def main():
    charger_styles_css()
    initialiser_session()
    st.title('Apprentissage interactif pour enfant')

    if st.session_state.quitter:
        st.markdown("### Merci d'avoir participé à cet apprentissage interactif ! 😊")
        st.markdown("Vous pouvez toujours reprendre en cliquant sur le bouton **Reprendre** ci-dessus.")
        if st.button("Reprendre"):
            recommencer()
    else:
        afficher_question()
        
        # Affichage des boutons dans des colonnes
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.button("Afficher la réponse", on_click=bouton_voir_reponse)
        with col2:
            st.button("Précédent", on_click=bouton_precedent)
        with col3:
            st.button("Suivant", on_click=bouton_suivant)
        with col4:
            st.button("Ressayer", on_click=bouton_cacher_reponse) 
        
        col5, col6, col7, col8 = st.columns(4)
        with col5:
            st.button("Classer", on_click=bouton_classer)
        with col6:
            st.button("Jeter ", on_click=bouton_jeter)
        with col7:
            pass # Ajouter un espace vide pour aligner les boutons
        with col8:
            pass # Ajouter un espace vide pour aligner les boutons
        
        # Bouton pour quitter
        if st.button("Quitter", on_click=bouton_quitter):
            setattr(st.session_state, 'quitter', True)

def bouton_quitter():
    setattr(st.session_state, 'quitter', True)



  
if __name__ == '__main__':
    main()
