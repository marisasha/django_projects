// external
import { constructorConstant } from "../components/components";

export const isDebug = true; // TODO - найти способ, автоматически
export const host = "http://127.0.0.1:8000";

// book
export const categoryList = constructorConstant("categoryList");
export const startapList = constructorConstant("startapList")
export const startapDetail = constructorConstant("startapDetail")
export const startapCreate = constructorConstant("startapCreate")
export const bookList = constructorConstant("bookList");
export const bookCreate = constructorConstant("bookCreate");
export const bookDetail = constructorConstant("bookDetail");
export const bookUpdate = constructorConstant("bookUpdate");
export const bookDelete = constructorConstant("bookDelete");

// user
export const userRegister = constructorConstant("userRegister");
export const userRegister2 = constructorConstant("userRegister2");
export const userLogin = constructorConstant("userLogin");
export const userDetail = constructorConstant("userDetail");
export const userUpdate = constructorConstant("userUpdate");
export const userProfile = constructorConstant("userProfile");
