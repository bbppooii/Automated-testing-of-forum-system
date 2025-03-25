import time
from common.Utils import Driver
from cases import Login,PersonalHomepage,Edit,Detail,PrivateMessage,HomePage,MyPost,Register

# 运行登录相关的测试
def run_Login_tests():
    """执行所有登录相关的测试"""
    login = Login.Login()  # 只实例化一次，避免重复创建对象
    login.login_suc_test1()
    login.login_suc_test2()
    login.test_login_empty_username_empty_password()
    login.test_login_empty_username_valid_password()
    login.test_login_empty_username_invalid_password()
    login.test_login_invalid_username_empty_password()
    login.test_login_valid_username_empty_password()
    login.test_login_valid_username_invalid_password()
    login.test_login_invalid_username_valid_password()
    login.test_login_invalid_username_invalid_password()

# 运行个人主页相关的测试
def run_PersonalHomepage_tests():
    """执行所有个人主页相关的测试"""
    personal_home = PersonalHomepage.PersonalHomepage()
    personal_home.test_switch_section()
    personal_home.test_search_input()
    personal_home.test_toggle_day_night_mode()
    personal_home.test_message_button()
    personal_home.test_user_profile()
    personal_home.test_change_avatar()
    personal_home.test_nickname_field()
    personal_home.test_email_field()
    personal_home.test_phone_number_field()
    personal_home.test_bio_field()
    personal_home.test_change_password()

# 运行帖子编辑相关的测试
def run_Edit_tests():
    """执行所有帖子编辑相关的测试"""
    edit = Edit.Edit()
    edit.Content_Box()
    edit.Title_Bar()
    edit.Plate_Selection()
    edit.Release()
    edit.test_switch_section()
    edit.test_search_input()
    edit.test_toggle_day_night_mode()
    edit.test_message_button()
    edit.test_user_profile()

# 运行帖子详情相关的测试
def run_Detail_tests():
    """执行所有帖子详情页面相关的测试"""
    detail = Detail.Detail()
    detail.Private_Message()
    detail.Post()
    detail.Comment()
    detail.Likes()
    detail.test_switch_section()
    detail.test_search_input()
    detail.test_toggle_day_night_mode()
    detail.test_message_button()
    detail.test_user_profile()

# 运行私信功能的测试
def run_PrivateMessage_tests():
    """执行私信功能的测试"""
    private_msg = PrivateMessage.PrivateMessage()
    private_msg.reply()

# 运行首页相关的测试
def run_HomePage_tests():
    """执行所有首页相关的测试"""
    home = HomePage.HomePage()
    home.Button()
    home.List()
    home.test_switch_section()
    home.test_search_input()
    home.test_toggle_day_night_mode()
    home.test_message_button()
    home.test_user_profile()

# 运行“我的帖子”相关的测试
def run_MyPost_test():
    """执行所有‘我的帖子’相关的测试"""
    my_post = MyPost.MyPost()
    my_post.Name()
    my_post.Post()
    my_post.test_switch_section()
    my_post.test_search_input()
    my_post.test_toggle_day_night_mode()
    my_post.test_message_button()
    my_post.test_user_profile()

# 运行注册功能的测试
def run_Register_test():
    """执行所有注册功能的测试"""
    register = Register.Register()
    register.test_valid_inputs_agree_terms()
    register.test_valid_username_empty_others_disagree_terms()
    register.test_empty_username_valid_nickname_mixed_passwords_disagree_terms()
    register.test_empty_username_nickname_valid_password_agree_terms()
    register.test_valid_inputs_missing_confirm_password_disagree_terms()
    register.test_valid_username_empty_nickname_password_confirmed_agree_terms()
    register.test_invalid_inputs_disagree_terms()

# 运行所有测试
def run_all_tests():
    """依次执行所有的测试，并在结束后关闭 WebDriver"""
    try:
        run_Login_tests()
        run_PersonalHomepage_tests()
        run_Edit_tests()
        run_Detail_tests()
        run_PrivateMessage_tests()
        run_HomePage_tests()
        run_MyPost_test()
        run_Register_test()
    except Exception as e:
        print(f"错误发生: {e}")  # 捕获异常，避免测试中断
    finally:
        Driver.driver.quit()  # 测试完成后关闭 WebDriver

# 主函数
if __name__ == '__main__':
    run_all_tests()