from  main import User,session,engine

# def updateData():
#     try:
#         local_session = session(bind=engine)
#         user_to_update = local_session.query(User).filter(User.username=="Ashis Singh").first()
#         user_to_update.username = "Ashis"
#         user_to_update.email = "Ashis.Singh000@gmail.com"
#         local_session.commit()
#     except Exception as ex:
#         print(ex)
# updateData()

class UpdateData:
    def updateData(self):
        try:
            self.local_session = session(bind=engine)
            self.user_to_update = self.local_session.query(User).filter(User.username == "My111").first()
            self.user_to_update.username = "Hi1233"
            self.user_to_update.email = "sfgsgdfg.Mf000@gmail.com"
            self.local_session.commit()
        except Exception as ex:
            print(ex)

update = UpdateData()
update.updateData()