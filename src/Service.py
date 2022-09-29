from src.Models.AdminUser import AdminUser
from src.Models.GroupMessageActions import GroupMessageActions
from src.Models.GroupUser import GroupUser
from src.Models.NormalUser import NormalUser

adminUser = AdminUser()
adminUser.login("adminUserID")
adminUser.createUser("newUser")

normalUser = NormalUser()
normalUser.login("normalUserId")
normalUser.createUser("newUser")


groupUser = GroupUser()
groupUser.createGroup("groupName")
groupUser.addInGroup("groupName")
groupUser.searchInGroup("name")


groupMessageActions = GroupMessageActions()
message = groupMessageActions.sendMessage("userID","Hi")
groupMessageActions.reactToMessage(message,normalUser,"Liked")


