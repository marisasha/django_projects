import { configureStore } from "@reduxjs/toolkit";
import * as components from "./components";
import * as constants from "./constants";
export const store = configureStore({
  reducer: {
    // @ts-ignore
    bookCreate: components.constructorReducer(constants.bookCreate),
    // @ts-ignore
    bookList: components.constructorReducer(constants.bookList),
    // @ts-ignore
    startapList: components.constructorReducer(constants.startapList),
    // @ts-ignore
    startapDetail: components.constructorReducer(constants.startapDetail),
    // @ts-ignore
    categoryList: components.constructorReducer(constants.categoryList),
    // @ts-ignore
    startapCreate: components.constructorReducer(constants.startapCreate),
    // @ts-ignore
    bookDetail: components.constructorReducer(constants.bookDetail),
    // @ts-ignore
    bookUpdate: components.constructorReducer(constants.bookUpdate),
    // @ts-ignore
    bookDelete: components.constructorReducer(constants.bookDelete),
    // user
    // @ts-ignore
    userRegister: components.constructorReducer(constants.userRegister),
    // @ts-ignore
    userRegister2: components.constructorReducer(constants.userRegister2),
    // @ts-ignore
    userLogin: components.constructorReducer(constants.userLogin),
    // @ts-ignore
    userDetail: components.constructorReducer(constants.userDetail),
    // @ts-ignore
    userUpdate: components.constructorReducer(constants.userUpdate),
    // @ts-ignore
    userProfile: components.constructorReducer(constants.userProfile),

  },
});
export default store;
