import streamlit as st
import random
import time

# Cấu hình trang
st.set_page_config(
    page_title="Trò Chơi Chải Lông Mèo Thần Tốc 🐱",
    page_icon="🐱",
    layout="centered"
)

# Khởi tạo Session State
if "fur_coins" not in st.session_state:
    st.session_state.fur_coins = 10       # Số lông mèo thu thập được (dùng làm tiền mua hàng)
if "cat_state" not in st.session_state:
    st.session_state.cat_state = "back"   # "back": quay lưng (được chải), "front": quay mặt (nguy hiểm)
if "last_action_time" not in st.session_state:
    st.session_state.last_action_time = time.time()
if "anger_count" not in st.session_state:
    st.session_state.anger_count = 0      # Số lần bị mèo giận
if "buff_active" not in st.session_state:
    st.session_state.buff_active = None   # "pate", "wool", "catnip"
if "buff_expire_time" not in st.session_state:
    st.session_state.buff_expire_time = 0
if "inventory" not in st.session_state:
    st.session_state.inventory = {"pate": 0, "wool": 0, "catnip": 0}
if "current_fortune" not in st.session_state:
    st.session_state.current_fortune = "Nhấn nút 'Bốc quẻ may mắn' để nhận lời khuyên hôm nay nhé!"

# Danh sách 20 quẻ/lời chúc tích cực
FORTUNES = [
    ("Học tập", "Thuận buồm xuôi gió, điểm cao phơi phới, tương lai rộng mở!"),
    ("Học tập", "Sự tập trung cao độ giúp bạn chinh phục mọi kỳ thi một cách dễ dàng."),
    ("Học tập", "Kiến thức tích lũy hôm nay sẽ nở hoa kết trái vào ngày mai."),
    ("Sức khỏe", "Thân thể khỏe mạnh, tràn đầy năng lượng tích cực suốt cả ngày dài."),
    ("Sức khỏe", "Tinh thần sảng khoái, ăn ngon ngủ yên, vạn sự hanh thông."),
    ("Sức khỏe", "Năng lượng dồi dào, vượt qua mọi mệt mỏi một cách nhẹ nhàng."),
    ("May mắn", "Quý nhân phù trợ, đi đến đâu cũng gặp may mắn, thuận lợi."),
    ("May mắn", "Cơ hội lớn đang gõ cửa, hãy tự tin đón nhận những điều tuyệt vời."),
    ("May mắn", "Vận may tài lộc mỉm cười, tiền vào như nước, bình an vô sự."),
    ("Gia đình", "Gia đạo bình an, tiếng cười ngập tràn, yêu thương gắn kết."),
    ("Gia đình", "Người thân luôn là bến bờ bình yên và là hậu phương vững chắc nhất của bạn."),
    ("Gia đình", "Mối quan hệ gia đình ngày càng thấu hiểu, ấm áp và gắn bó bền chặt."),
    ("Mối quan hệ", "Hòa hợp với mọi người, đi đến đâu cũng kết giao được bạn tốt."),
    ("Mối quan hệ", "Tình cảm thăng hoa, các mối quan hệ xung quanh đều vô cùng tốt đẹp."),
    ("Mối quan hệ", "Lời nói chân thành giúp bạn ghi điểm tuyệt đối trong mắt mọi người."),
    ("Tinh thần", "Hôm nay là một ngày tuyệt vời để bắt đầu những dự định mới!"),
    ("Tinh thần", "Sự tự tin là chìa khóa mở cánh cửa thành công cho bạn."),
    ("Tinh thần", "Mỗi thử thách vượt qua là một bước tiến lớn giúp bạn trưởng thành hơn."),
    ("May mắn", "Hạnh phúc gõ cửa từ những điều nhỏ nhặt nhất trong cuộc sống."),
    ("Học tập", "Tư duy sáng tạo bùng nổ, giải quyết mọi bài toán khó một cách xuất sắc.")
]

# Kiểm tra thời gian hiệu lực của Buff (Pate, Len, Cỏ mèo)
current_time = time.time()
if st.session_state.buff_active and current_time > st.session_state.buff_expire_time:
    st.session_state.buff_active = None

# Tự động đổi trạng thái mèo nếu không có buff
if not st.session_state.buff_active:
    # Nếu quá 3-6 giây thì mèo có thể quay đầu ngẫu nhiên
    if current_time - st.session_state.last_action_time > random.randint(3, 6):
        if st.session_state.cat_state == "back":
            st.session_state.cat_state = "front"
        else:
            st.session_state.cat_state = "back"
        st.session_state.last_action_time = current_time
else:
    # Nếu có buff, mèo luôn quay lưng (hoặc mải chơi)
    st.session_state.cat_state = "back"

# Giao diện chính
st.title("🐱 Trò Chơi Chải Lông Mèo & Bốc Quẻ May Mắn")
st.audio("aaf63b4ec0940a2a6a4ad5f7b9786871.mp4", autoplay=True, loop=True)


# Chia tab cho gọn gàng
tab1, tab2, tab3 = st.tabs(["🎮 Game Chải Lông", "🛒 Cửa Hàng Vật Phẩm", "📜 Bốc Quẻ May Mắn"])

with tab1:
    st.subheader("Trò chơi: Chải Lông Mèo Thần Tốc")
    st.write("💡 **Luật chơi:** Khi mèo quay lưng (`🐈‍⬛`), hãy nhanh tay chải lông để thu thập 🧶 Lông Mèo. Khi mèo quay mặt lại (`🐈`), bạn phải dừng ngay lập tức, nếu không mèo sẽ giận dữ!")

    # Hiển thị trạng thái Buff nếu có
    if st.session_state.buff_active == "pate":
        st.info("🍲 Mèo đang mải ăn pate, hoàn toàn chú tâm và không quay đầu trong 45 giây!")
    elif st.session_state.buff_active == "wool":
        st.info("🧶 Mèo đang say sưa vờn cục len, yên tâm chải lông trong 1 phút 25 giây!")
    elif st.session_state.buff_active == "catnip":
        st.success("🌿 Mèo đang phê cỏ mèo, cực kỳ dễ chịu và đứng im trong 2 phút 30 giây!")

    # Hiển thị hình ảnh mèo tương ứng
    col_m1, col_m2, col_m3 = st.columns([1, 2, 1])
    with col_m2:
        if st.session_state.cat_state == "back":
            st.markdown("<h1 style='text-align: center; font-size: 100px;'>🐈‍⬛</h1>", unsafe_allow_html=True)
            st.image("7c59985cb967810af105286709184ba2.jpg", use_container_width=True)
            st.markdown("<p style='text-align: center; color: green;'><b>Mèo đang quay lưng (An toàn để chải!)</b></p>", unsafe_allow_html=True)
        else:
            st.markdown("<h1 style='text-align: center; font-size: 100px;'>🐈</h1>", unsafe_allow_html=True)
            st.image("6b73b5cf4a17da8304ac0ac0d3e19642.jpg", use_container_width=True)
            st.markdown("<p style='text-align: center; color: red;'><b>⚠️ MÈO ĐANG QUAY MẶT LẠI! DỪNG CHẢI NGAY!</b></p>", unsafe_allow_html=True)

    # Hiển thị tài nguyên
    st.metric("🧶 Lông mèo thu thập được (Tiền tệ)", f"{st.session_state.fur_coins} sợi")
    st.error(f"💢 Số lần làm mèo giận: {st.session_state.anger_count}/5")

    # Nút chải lông
    if st.button("🪮 Chải Lông Ngay!", use_container_width=True):
        if st.session_state.cat_state == "back" or st.session_state.buff_active is not None:
            earned = random.randint(1, 3)
            st.session_state.fur_coins += earned
            st.success(f"✨ Chải thành công! Bạn thu thập được +{earned} sợi lông mèo.")
        else:
            st.session_state.anger_count += 1
            st.session_state.fur_coins = max(0, st.session_state.fur_coins - 2)
            st.error("😾 Bị phát hiện! Mèo quay mặt lại cào bạn và bạn bị trừ 2 sợi lông!")
            if st.session_state.anger_count >= 5:
                st.warning("😿 Mèo đã giận bỏ đi mất tiêu! Đã reset trạng thái game.")
                st.session_state.anger_count = 0
                st.session_state.fur_coins = 5

    if st.button("🔄 Làm mới trạng thái game"):
        st.rerun()

with tab2:
    st.subheader("🛒 Cửa Hàng Vật Phẩm Dụ Mèo")
    st.write("Dùng số lông mèo thu thập được để mua các món đồ giúp mèo ngoan ngoãn:")

    col_s1, col_s2, col_s3 = st.columns(3)

    with col_s1:
        st.markdown("### 🍲 Pate Mèo")
        st.write("Giúp mèo ăn ngon miệng, không quan tâm bạn trong **45 giây**.")
        st.write("💰 **Giá:** 10 sợi lông")
        if st.button("Mua & Dùng Pate"):
            if st.session_state.fur_coins >= 10:
                st.session_state.fur_coins -= 10
                st.session_state.buff_active = "pate"
                st.session_state.buff_expire_time = time.time() + 45
                st.success("Đã cho mèo ăn Pate thành công!")
                st.rerun()
            else:
                st.error("Không đủ lông mèo để mua!")

    with col_s2:
        st.markdown("### 🧶 Cục Len")
        st.write("Mèo mải vờn len, không để ý bạn trong **1 phút 25 giây** (85s).")
        st.write("💰 **Giá:** 20 sợi lông")
        if st.button("Mua & Dùng Len"):
            if st.session_state.fur_coins >= 20:
                st.session_state.fur_coins -= 20
                st.session_state.buff_active = "wool"
                st.session_state.buff_expire_time = time.time() + 85
                st.success("Đã tặng cục len cho mèo!")
                st.rerun()
            else:
                st.error("Không đủ lông mèo để mua!")

    with col_s3:
        st.markdown("### 🌿 Cỏ Mèo")
        st.write("Mèo phê cỏ cực phấn khích, không quan tâm bạn trong **2 phút 30 giây** (150s).")
        st.write("💰 **Giá:** 35 sợi lông")
        if st.button("Mua & Dùng Cỏ Mèo"):
            if st.session_state.fur_coins >= 35:
                st.session_state.fur_coins -= 35
                st.session_state.buff_active = "catnip"
                st.session_state.buff_expire_time = time.time() + 150
                st.success("Đã cho mèo thưởng thức cỏ mèo!")
                st.rerun()
            else:
                st.error("Không đủ lông mèo để mua!")

with tab3:
    st.subheader("📜 Bốc Quẻ May Mắn Hằng Ngày")
    st.write("Tính năng riêng biệt giúp dự báo những điều tích cực về Học tập, Sức khỏe, May mắn, Gia đình và Mối quan hệ xung quanh bạn!")

    if st.button("🥠 Lắc ống quẻ / Bốc quẻ ngay", use_container_width=True):
        category, content = random.choice(FORTUNES)
        st.session_state.current_fortune = f"**[{category}]** {content}"

    # Hiển thị kết quả quẻ
    st.info(st.session_state.current_fortune)
    st.caption("✨ Tất cả các quẻ đều mang ý nghĩa tích cực, chúc bạn một ngày tràn đầy năng lượng và bình an!")
