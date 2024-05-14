// external
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { useEffect } from "react";
import * as constants from "./constants";
import * as utils from "./utils";

export function Navbar() {
  const userLogin = useSelector((state: any) => state.userLogin);
  const dispatch = useDispatch();
  useEffect(() => {
    if (utils.LocalStorage.get("userLogin.data.access")) {
      dispatch({
        type: constants.userLogin.success,
        payload: {
          access: utils.LocalStorage.get("userLogin.data.access"),
          refresh: utils.LocalStorage.get("userLogin.data.refresh"),
        },
      });
    }
  }, []);

  return (
      <nav className="m-0 flex items-center justify-between bg-yellow-500 w-full px-10" aria-label="Global">
        <div className="flex gap-x-12 items-center">
              <Link to="/" className="text-sm font-semibold leading-6 text-slate-50 hover:text-gray-600 flex gap-x-2 items-center">
                <i className="fa-sharp fa-solid fa-house"></i>
                  <span>Главная </span>
              </Link>
              {userLogin && userLogin.data ? (
                
                <div className="flex gap-x-12">
                  <Link to="/create" className="text-sm font-semibold leading-6 text-slate-50 hover:text-gray-600 flex gap-x-2 items-center">
                    <i className="fa-sharp fa-solid fa-plus"></i>
                    <span>Опубликовать проект </span>
                  </Link>

                  <Link to="/profile" className="text-sm font-semibold leading-6 text-slate-50 hover:text-gray-600 flex gap-x-2 items-center">
                    <i className="fa-solid fa-user"></i>
                    <span>Профиль</span>
                  </Link>
                </div>
                


              ):""}
        </div>
  
        <div className="flex flex-col gap-y-2 w-48 h-16 justify-center " >
            {userLogin && userLogin.data ? (
                
                <Link to="/logout" className=" flex gap-x-2 text-sm font-semibold leading-6 text-slate-50 hover:text-red-600 flex gap-x-2 items-center">
                  <i className="fa-solid fa-right-from-bracket m-0"></i>
                  Выйти
                </Link>
            ) : (
              <div className="flex flex-col ">
                <Link to="/login" className="flex  gap-x-2 text-sm font-semibold leading-6 text-slate-50 hover:text-green-600 flex gap-x-2 items-center">
                  <i className ="fa-solid fa-arrow-right-to-bracket"></i>
                  Войти
                </Link>
                <Link to="/register" className="text-sm font-semibold leading-6 text-slate-50 hover:text-blue-600 flex gap-x-1 items-center">
                  <i className="fa-solid fa-user-plus  m-0"></i>
                  Регистрация
                </Link>
              </div>
            )}
          </div>
      </nav>
  );
  }
