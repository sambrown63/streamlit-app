import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emojis-cheat-sheet/
st.set_page_config(page_title="BrownFur", page_icon=":tada:", layout="wide")

# SIDEBAR
with st.sidebar:
    selected = option_menu(
        menu_title=None, #required
        options=["Home","About", "Contact"], #required
    )

    img = Image.open("image/sam.jpg")

if selected == "About":
    st.title("About")
    st.image(img)
    st.write("##")
    st.subheader("hi my name is sam, i'm a teenager from ghana and i'm looking for a job as a hacker. if you have any jobs for me feel free to contact me")
if selected == "Contact":
    st.write("You can contact me by telegram or follow me on X")
    st.write("##")
    st.markdown("[telegram](t.me/Susuyg)")
    st.markdown("[X](https://x.com/sambrown1000)")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/b0582a6c-ae65-4474-9b75-c4b81c5985fc/infk05OCgX.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Sam :wave:")
    st.title("A Teenager From Ghana")
    st.write("I am passionate about finding things do,I'm also a fun guy who like's gaming,and WWE,Football(soccer) Fun")
    st.write("[Learn More >](https://x.com/SamBrown1000)")

# --- WHAT I DO ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my X account I talk about:
            - gaming
            - hacking
            - life update
            - wwe

            If this sounds interesting to you, consider checking my account and turn on the notifications, so you can stay upto date.
            """
    )
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("About")
    st.write("##")
    image_column, text_column = st. columns(2)
    with text_column:
        st.subheader("I upload some projects to github")
        st.write(
            """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eleifend pellentesque mi. Mauris sodales elit eu justo interdum, eget lobortis lorem interdum. Integer interdum blandit ipsum, a tincidunt augue eleifend vitae. Phasellus est nulla, gravida ac maximus id, vehicula eget mi. Vestibulum viverra, ipsum non maximus bibendum, velit massa vehicula tortor, non elementum quam urna quis eros. Integer non mollis leo, in dignissim lectus. In mollis tellus sed turpis egestas suscipit. Phasellus in faucibus orci. Quisque sit amet sem vitae orci tincidunt finibus. Donec ligula augue, consectetur id augue sit amet, eleifend fermentum ante. Nam a consectetur justo, vitae volutpat ligula. Donec luctus mauris nibh, a efficitur justo dignissim sed. In in elementum nibh. Nam vitae sollicitudin lorem. Etiam congue dui id mi vestibulum, at varius velit lacinia. Quisque eget diam eu nisi iaculis accumsan non in sapien.

Mauris maximus, sapien quis aliquet luctus, metus purus vestibulum mauris, non eleifend neque nunc sed ante. Nam non neque metus. Cras sed blandit turpis, eget malesuada ex. Pellentesque nec bibendum nibh. Aenean velit tortor, eleifend quis facilisis sed, porttitor ac diam. Suspendisse sit amet quam at nunc ornare sagittis varius ac tellus. Etiam tempus molestie purus quis efficitur.

Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent nec cursus tellus, ut faucibus orci. Phasellus porttitor massa ut pharetra pharetra. Mauris fermentum accumsan cursus. In lacus mi, molestie in libero eget, congue hendrerit odio. Donec eget accumsan sem. Etiam eros nisi, sollicitudin eget nulla ut, finibus luctus arcu. Donec aliquam semper egestas. Mauris sed massa vitae nunc volutpat pellentesque. Fusce non ligula vitae nibh volutpat facilisis sit amet tristique mi. Pellentesque quis dapibus velit, in facilisis nulla.

Mauris in mattis felis. Nam rhoncus velit sapien. Phasellus urna mauris, facilisis malesuada scelerisque ut, viverra a odio. In pulvinar odio facilisis sollicitudin laoreet. Sed ullamcorper vulputate est. Aliquam vitae efficitur elit, eu luctus dolor. Duis dapibus odio tincidunt, dictum massa a, maximus neque. Integer nec orci et urna auctor bibendum. Integer lectus arcu, commodo sed sapien id, mattis pretium lacus. Nulla condimentum tincidunt mi, venenatis auctor elit. Curabitur vehicula lorem sapien. Cras sollicitudin neque orci, vitae tristique metus convallis ac. Donec fringilla felis non urna mollis finibus.

Vivamus purus neque, vestibulum at orci sed, interdum elementum neque. Donec eu diam malesuada, rutrum turpis in, mattis ex. Fusce malesuada orci non purus mollis, a luctus nibh dapibus. Fusce eu lorem ullamcorper, ultricies urna scelerisque, lacinia sem. Aliquam vitae nulla diam. Donec non ante id libero tempus placerat. Fusce imperdiet risus et nibh efficitur accumsan. Duis id nulla feugiat, luctus leo nec, sodales magna. Aenean laoreet in ex non lacinia. Pellentesque ut nisi sed nibh molestie vestibulum quis a sapien.

Curabitur justo sapien, luctus ut velit nec, mollis ullamcorper magna. Aenean faucibus posuere gravida. Donec consequat velit ut ornare commodo. Quisque sit amet condimentum mi, sit amet suscipit est. Ut ut urna velit. In bibendum urna odio, eu accumsan mi ornare volutpat. Donec congue sollicitudin velit. Aenean sapien eros, pulvinar ut arcu non, feugiat pellentesque nisl.

Cras quis feugiat massa. Ut volutpat accumsan tellus a finibus. Cras tempor nec risus vel sagittis. Praesent ullamcorper nunc vel aliquet euismod. Aenean ipsum arcu, pretium in tincidunt eu, euismod ut orci. Fusce porttitor congue magna in viverra. Aliquam orci justo, commodo interdum rutrum non, iaculis et dolor.
            """
        )
        st.markdown("[Github...](https://github.com/sambrown63/")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https//formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/sambrown6366@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns((1, 2))
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()