import { configureStore } from "@reduxjs/toolkit";
import * as components from "./components";
import * as constants from "./constants";
export const store = configureStore({
  reducer: {
    // @ts-ignore
    startapList: components.constructorReducer(constants.startapList),
    // @ts-ignore
    startapDetail: components.constructorReducer(constants.startapDetail),
    // @ts-ignore
    categoryList: components.constructorReducer(constants.categoryList),
    // @ts-ignore
    startapCreate: components.constructorReducer(constants.startapCreate),
    // @ts-ignore
    userRegister: components.constructorReducer(constants.userRegister),
    // @ts-ignore
    userRegister2: components.constructorReducer(constants.userRegister2),
    // @ts-ignore
    userLogin: components.constructorReducer(constants.userLogin),
    // @ts-ignore
    userUpdate: components.constructorReducer(constants.userUpdate),
    // @ts-ignore
    userProfile: components.constructorReducer(constants.userProfile),

  },
});
export default store;
