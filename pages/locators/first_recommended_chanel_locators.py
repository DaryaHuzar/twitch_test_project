from selenium.webdriver.common.by import By

user_menu_toggle = (By.CSS_SELECTOR, 'button[data-a-target="user-menu-toggle"]')
dark_mode_toggle = (By.CSS_SELECTOR, 'div[data-a-target="dark-mode-toggle"]')
language_button = (By.CSS_SELECTOR, 'button[data-a-target="language-dropdown-link"]')
english_language = (By.CSS_SELECTOR, 'button[data-a-target="language-en"]')
check_english_language = (By.CSS_SELECTOR, 'button[aria-label="Follow"]')
theatre_mode_button = (By.CSS_SELECTOR, 'button[data-a-target="player-theatre-mode-button"]')
check_theatre_mode = (By.CSS_SELECTOR, 'div[data-a-player-state="theatre"]')
full_screen_button = (By.CSS_SELECTOR, 'button[data-a-target="player-fullscreen-button"]')
check_fullscreen_mode = (By.CSS_SELECTOR, 'button[aria-label="Обычный режим (f)"]')
settings_button = (By.CSS_SELECTOR, 'button[data-a-target="player-settings-button"]')
quality_video_button = (By.CSS_SELECTOR, 'button[data-a-target="player-settings-menu-item-quality"]')
field_of_settings = (By.CSS_SELECTOR, 'div[data-a-target="player-settings-menu"]')
list_of_video_qualities = (By.CSS_SELECTOR, 'div[class="Layout-sc-1xcs6mc-0 beAYWq"]')
quality_video_check = (By.CLASS_NAME, 'kLZqyf')
indicator_of_mini_player = (By.CSS_SELECTOR, 'div[data-a-target="player-settings-submenu-advanced-toggle-mini"]')
mini_player_window = (By.CLASS_NAME, 'video-player__overlay')
stream_screen = (By.CLASS_NAME, 'stream-display-ad__wrapper')
pause_play_button = (By.CSS_SELECTOR, 'button[data-a-target="player-play-pause-button"]')
pause_message = (By.CSS_SELECTOR, 'button[aria-label="Воспроизведение (пробел/k)"]')
start_watching = (By.CSS_SELECTOR, 'button[data-a-target="player-overlay-mature-accept"]')
mute_button = (By.CSS_SELECTOR, 'button[aria-label="Выкл. звук (m)"]')
advanced_button = (By.CSS_SELECTOR, 'button[data-a-target="player-settings-menu-item-advanced"]')
advanced_settings_field = (By.CSS_SELECTOR, 'div[data-a-target="player-settings-menu"]')
video_statistics_window = (By.CSS_SELECTOR, 'table[class="Table-sc-602hti-0 feFOCU tw-table"]')
view_button = (By.CLASS_NAME, 'navigation-link')
report_a_bug_button = (By.CSS_SELECTOR, 'button[data-a-target="player-settings-menu-item-report"]')
select_report = (
    By.CSS_SELECTOR, 'select[class="ScInputBase-sc-vu7u7d-0 ScSelect-sc-gz38t2-0'
                     ' gXVFsI AJDRH InjectLayout-sc-1i43xsx-0 bLZRbT tw-select"]', '«Заикание» звука и изображения')
first_report = (By.CSS_SELECTOR, 'option[value="stutter-both"]')
settings_menu_field = (By.CSS_SELECTOR, 'div[data-a-target="player-settings-menu"]')
list_of_hotkeys = (By.CLASS_NAME, 'tw-table-body')
open_chat_button = (By.CSS_SELECTOR, 'button[aria-label="Развернуть чат"]')
close_chat_button = (By.CSS_SELECTOR, 'button[aria-label="Свернуть чат"]')
chat_rules_ok_button = (By.CSS_SELECTOR, 'button[data-test-selector="chat-rules-ok-button"]')
message_to_chat_field = (By.CSS_SELECTOR, 'textarea[data-a-target="chat-input"]')
join_to_twitch_window = (By.CSS_SELECTOR, 'div[data-a-target="passport-modal"]')
community_button = (By.CSS_SELECTOR, 'button[data-test-selector="chat-viewer-list"]')
filter_field = (By.CSS_SELECTOR, 'div[class="tw-search-input"]')
spectators_button = (By.CSS_SELECTOR, 'button[class="InjectLayout-sc-1i43xsx-0 daSCXI"]')
spectators_field = (By.CSS_SELECTOR, 'div[class="Layout-sc-1xcs6mc-0 hvqWsm"]')
chat_settings_button = (By.CSS_SELECTOR, 'button[data-a-target="chat-settings"]')
chat_filter_button = (By.CSS_SELECTOR, 'button[data-test-selector="chat-filter-item-click-target"]')
enable_filtration_in_chat = (By.CSS_SELECTOR, 'div[data-test-selector="chat-filter-top-toggle"]')
community_points_button = (By.CSS_SELECTOR, 'div[data-test-selector="community-points-summary"]')
channel_points_reward = (By.ID, 'channel-points-reward-center-body')
follow_button = (By.CSS_SELECTOR, 'button[data-a-target="follow-button"]')
subscription_info = (By.CSS_SELECTOR, 'div[class="Layout-sc-1xcs6mc-0 jnwfls support-panel-container"]')
subscribe_button = (By.CSS_SELECTOR, 'button[data-test-selector="subscribe-button__dropdown"]')
sing_in_window = (By.CSS_SELECTOR, 'div[data-a-target="passport-modal"]')
subscribe_main_button = (By.CSS_SELECTOR, 'button[aria-label="Подписаться $4.99"]')
donate_a_subscription_field = (By.CLASS_NAME, 'cvoaeL')
gift_for_community_window = (By.CLASS_NAME, 'jnwfls')
show_love_button = (By.CSS_SELECTOR, 'img[alt="showlove"]')
show_love_gif = (By.CSS_SELECTOR, 'div[aria-label="Оверлей «showlove»"]')
party_button = (By.CSS_SELECTOR, 'img[alt="party"]')
party_gif = (By.CSS_SELECTOR, 'div[aria-label="Оверлей «party»"]')
lul_button = (By.CSS_SELECTOR, 'img[alt="lul"]')
lul_gif = (By.CSS_SELECTOR, 'div[aria-label="Оверлей «lul»"]')
biblethump_button = (By.CSS_SELECTOR, 'img[alt="biblethump"]')
biblethump_gif = (By.CSS_SELECTOR, 'div[aria-label="Оверлей «biblethump»"]')
share_button = (By.CSS_SELECTOR, 'button[data-a-target="share-button"]')
share_field = (By.CSS_SELECTOR, 'div[role="dialog"]')
report_button = (By.CSS_SELECTOR, 'button[data-a-target="report-button-more-button"]')
report_translation_button = (By.CSS_SELECTOR, 'button[aria-label="Пожаловаться на трансляцию"]')
report_other_button = (By.CSS_SELECTOR, 'button[aria-label="Отправить другую жалобу"]')
searching_field = (By.CSS_SELECTOR, 'input[aria-label="Поисковый запрос"]')
dreadztv_chanel = (By.CSS_SELECTOR, 'a[href="/dreadztv"]')
collapse_recommended_channels = (By.CSS_SELECTOR, 'button[data-a-target="side-nav-arrow"]')
side_nav_header_collapsed = (By.CSS_SELECTOR, 'div[data-a-target="side-nav-header-collapsed"]')
show_more = (By.CSS_SELECTOR, 'button[data-test-selector="ShowMore"]')
show_less = (By.CSS_SELECTOR, 'button[data-test-selector="ShowLess"]')
logout_button = (By.CSS_SELECTOR, 'button[data-a-target="dropdown-logout"]')