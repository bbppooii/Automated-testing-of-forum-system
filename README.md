##论坛系统自动化测试  
本项目是基于SSM框架（Spring、Spring MVC、MyBatis）开发的论坛系统，包括 用户注册、登录、帖子发布、编辑、删除、查看 等功能，同时提供帖子列表页和详情页 供用户浏览论坛内容。   
用户登录后可以查看自己和其他用户的帖子，并通过系统 记录帖子发布时间、标题、作者信息。论坛支持 用户评论、私信交流、帖子点赞等社交互动功能，提升用户体验。  
为了确保系统的稳定性和功能完整性，项目采用 Selenium 自动化测试 进行功能验证，测试内容涵盖：  
用户注册与登录：测试不同输入情况下的账号验证逻辑  
帖子列表展示：确保帖子加载、排序和分页功能正常  
用户信息校验：验证用户个人资料、修改信息的功能  
帖子管理：测试帖子发布、编辑、删除是否符合预期  
帖子详情页：检查帖子的内容是否正确加载，包括评论、点赞等互动功能  
搜索功能：验证用户输入关键词后，搜索结果是否匹配  
本项目通过自动化测试覆盖核心功能，确保论坛系统在不同用户操作和高并发场景下的稳定性和可靠性，同时减少人工测试成本，提高测试效率。  

##运行环境  
Python 版本：3.13  
依赖库：selenium  
浏览器：Microsoft Edge  
版本 134.0.3124.68 (正式版本) (64 位)  
WebDriver：msedgedriver 需正确配置  

##运行方式  
安装 selenium  
依赖： 确保 msedgedriver 已正确安装。  
运行 Test.py 以执行完整的测试流程  

##详细可见  
