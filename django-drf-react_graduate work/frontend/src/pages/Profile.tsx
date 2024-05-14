// TODO external  //////////////////////////////////////////////////////////////////
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useParams } from "react-router-dom";
// TODO internal //////////////////////////////////////////////////////////////////
import * as bases from "../components/bases";
import * as components from "../components/components";
import * as constants from "../components/constants";
import * as store from "../components/store";
import * as loaders from "../components/loaders";
import * as utils from "../components/utils";


export default function Page() {
  // TODO hooks //////////////////////////////////////////////////////////////////
  const dispatch = useDispatch();
  const userProfile = useSelector((state: any) => state.userProfile);
  const username = utils.LocalStorage.get('username')
  
  
  async function getProfile() {
    if (!userProfile.load) {
      components.constructorWebAction(
        dispatch,
        constants.userProfile,
        `http://127.0.0.1:8000/api/profile/${username}`,
        "GET",
      );
    }
  }


  useEffect(() => {
    getProfile();
  }, []);


  return (
    <bases.Base1>

  <loaders.Loader1 isView={userProfile.load} />
          {userProfile.error && (
            <div className="alert alert-danger" role="alert">
              {userProfile.error}
            </div>
          )}
          {userProfile.fail && (
            <div className="alert alert-danger" role="alert">
              {userProfile.fail}
            </div>
          )}
      
          {!userProfile.load && userProfile.data ? (
              <div className="flex flex-col gap-y-10 mx-20 mt-20 pt-10 rounded-lg box-border">
                <h3 className="text-4xl font-bold leading-9 tracking-tight text-slate-50 m-auto">Ваш профиль:</h3>
                <div className="flex justify-between rounded w-full p-2 "> 
                  <div className="flex flex-col gap-y-12 w-1/2 ml-10 ">
                    <div className="flex flex-col gap-y-3">
                        <div className="flex gap-x-16 m-auto">
                          <div className="circular-avatar">
                            <img src={`/static${userProfile.data.avatar}`} alt="User Avatar" />
                          </div>
                            <div className="flex-col flex gap-y-2 justify-center">
                              <div className="flex gap-x-2">
                                <span className="text-xl text-slate-50 font-semibold">{userProfile.data.name}</span>
                                <span className="text-xl text-slate-50 font-semibold">{userProfile.data.surname}</span>
                              </div>
                              <span className="text-xl text-slate-50 font-semibold">Предприниматель</span>
                            </div>
                            <div className="flex flex-col justify-center items-center">
                              <span className="text-xl text-slate-50 font-semibold">Зарегистрирован:</span>
                              <span className="text-xl text-slate-50 font-semibold ">
                                {userProfile.data.data_register &&
                                  new Date(userProfile.data.data_register).toLocaleDateString('ru-RU', {
                                    day: 'numeric',
                                    month: 'long',
                                    year: 'numeric'
                                  })
                                }
                              </span>
                            </div>
                            <div className="flex flex-col justify-center items-center">
                              <div className="flex gap-x-2">
                                <span className="text-xl text-slate-50 font-semibold">Контактный</span>
                                <span className="text-xl text-slate-50 font-semibold"> номер:</span>
                              </div>
                              <span className="text-xl text-slate-50 font-semibold">{userProfile.data.number}</span>

                            </div>
                        </div>
                        <div className="flex flex-col gap-y-4 mt-10">
                          <h3 className="text-3xl font-bold leading-9 tracking-tight text-slate-50 ">Ваши проекты:</h3>
                          <div className="flex flex-col gap-y-5">
                            {!userProfile.load ? userProfile.data.startap.map((item: any, index: number) => (
                                  <div key = {item.id} className="rounded text-slate-800 mt-10 mr-10 shadow-xl">
                                    <Link to ={`/category/${item.category_slug}/${item.id}`} className= {`category flex  bg-slate-50 rounded w-11/12 h-80 `} >
                                      <img src={`/static${item.image}`} alt="" className="w-6/12 h-auto "/>
                                      <div className="flex flex-col ml-3">
                                        <span className="text-slate-900 text-3xl font-bold "> {item.title} </span>
                                        <span className="text-slate-500 text-l font-bold "> {item.category_title}  </span>
                                        <div>
                                          <i className ="fa-sharp fa-solid fa-location-dot bg-red "></i>
                                          <span className="text-slate-900 text-lg font-bold "> {item.location} </span>
                                        </div> 
                                      </div>
                                    </Link>
                                    </div>
                                  ))
                                  : ""}
                          </div>
                        </div>
                    </div>
                  </div>
                </div>
              </div>
          ):""
          }
        
    </bases.Base1>
  )
}
