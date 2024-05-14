// TODO external  //////////////////////////////////////////////////////////////////
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useParams } from "react-router-dom";
// TODO internal //////////////////////////////////////////////////////////////////
import * as bases from "../components/bases";
import * as utils from "../components/utils";
import * as components from "../components/components";
import * as constants from "../components/constants";
import * as store from "../components/store";
import * as loaders from "../components/loaders";
import axios from "axios";

export default function Page() {
  // TODO hooks //////////////////////////////////////////////////////////////////
  const dispatch = useDispatch();
  const startapDetail = useSelector((state: any) => state.startapDetail);
  const params = useParams();
  const username = utils.LocalStorage.get('username')
  const [showPdf, setShowPdf] = useState(false);
  const [showDownloads, setDownloads] = useState(false);
  const [buttonClicked, setButtonClicked] : any = useState(false);

  // TODO functions //////////////////////////////////////////////////////////////////
  async function getStartap() {
    if (!startapDetail.load) {
      components.constructorWebAction(
        dispatch,
        constants.startapDetail,
        `http://127.0.0.1:8000/api/${params.slug}/${params.id}`,
        "GET",
      );
    }
  }
  const getDownloads = () => {
    setDownloads(!showDownloads);
  };
  const sumBeaty = (num:any) => {
    num = String(num);
    for (let i = num.length - 3; i > 0; i -= 3) {
        num = num.slice(0, i) + ' ' + num.slice(i);
    }
    return num;
  }

  // TODO useEffect //////////////////////////////////////////////////////////////////
  useEffect(() => {
    getStartap();
  }, []);

  useEffect(() => {
    if (startapDetail.data && startapDetail.data.likes.length > 0 && startapDetail.data.likes.username === username) {
      setButtonClicked(true);
    }
  }, [startapDetail, username]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        if (startapDetail.data) {
          await axios.get(`http://127.0.0.1:8000/api/press_like/${startapDetail.data.id}/${username}`);
        }
      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
  }, [buttonClicked, startapDetail.data?.id, username]);

  return (
    <bases.Base1>

        <loaders.Loader1 isView={startapDetail.load} />
        {startapDetail.error && (
          <div className="alert alert-danger" role="alert">
            {startapDetail.error}
          </div>
        )}
        {startapDetail.fail && (
          <div className="alert alert-danger" role="alert">
            {startapDetail.fail}
          </div>
        )}
  
      
        {!startapDetail.load && startapDetail.data ? (
          <div className="flex flex-col gap-y-10 mx-20 mt-20 pt-10 bg-white rounded-lg  box-border">
            <span className="text-5xl text-gray-900 font-bold m-auto">{startapDetail.data.title}</span>     
            <hr />   
            <div className="flex justify-between rounded w-full p-2 "> 
                <div className="flex flex-col gap-y-12 w-1/2 ml-10 ">
                        <div className="flex flex-col gap-y-3">
                            <div className="flex gap-x-5">
                              <div className="circular-avatar">
                                <img src={`/static${startapDetail.data.profile.avatar}`} alt="User Avatar" />
                              </div>
                                <div className="flex-col flex gap-y-2 justify-center">
                                  <div className="flex gap-x-2">
                                    <span className="text-xl text-gray-900 font-semibold">{startapDetail.data.profile.name}</span>
                                    <span className="text-xl text-gray-900 font-semibold">{startapDetail.data.profile.surname}</span>
                                  </div>
                                  <span className="text-xl text-gray-900 font-semibold">Предприниматель</span>
                                </div>
                            </div>
                        </div>
                        
                        <div className="flex flex-col gap-y-3 w-full">

                          <span className="text-2xl text-gray-900 font-semibold">Описание проекта: </span>
                          <span className=" text-xl text-gray-900 ml-4 ">{startapDetail.data.description}</span>

                          <span className="text-2xl text-gray-900 font-semibold">Местоположение: </span>
                          <div>
                            <i className ="fa-sharp fa-solid fa-location-dot bg-red "></i>
                            <span className="text-slate-900 text-xl font-bold ml-4"> {startapDetail.data.location} </span>
                          </div> 

                          <span className="text-2xl text-gray-900 font-semibold">Необходимая сумма вложения: </span>
                          <span className=" text-4xl text-yellow-500 ml-4">{sumBeaty(startapDetail.data.deposit_amount)} RUB</span>

                          <span className="text-2xl text-gray-900 font-semibold">Контактный телефон: </span>
                          <span className=" text-xl text-gray-900  ml-4">{startapDetail.data.profile.number}</span>
              
                      </div>
                        
                        <div className="flex gap-x-2">
                          <div>
                            <button onClick={getDownloads} className="mb-3 flex w-30 justify-center rounded-md bg-yellow-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-gray-600 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 ">Дополнительные файлы</button>
                            { showDownloads ? startapDetail.data.files.map((item:any,index:number) => (
                              <div className="flex flex-col ">
                                <div className="flex items-center ml-3">
                                  <a href={`/static${item.file}`} download>
                                    <i className="fa-solid fa-circle-down text-green-500"></i>
                                  </a>
                                </div>
                              </div>
                            )) : ""}
                          </div>
                          
                      </div>
                  </div>
                    
                    <div className="flex flex-col w-1/2">
                      <embed src={`/static${startapDetail.data.pdf}`} width="800" height="400" className=""/>
                        {buttonClicked ?
                          <div className="flex gap-x-2 rounded-xl p-2 w-16 h-16 mt-10 bg-gray-500 hover:bg-yellow-500 ">
                            <button onClick={(()=>setButtonClicked(false))}><i className="fa-regular fa-heart text-5xl"></i></button>
                          </div>
                          :
                          <div className="flex gap-x-2 rounded-xl p-2 w-16 h-16 mt-10 bg-yellow-500 hover:bg-gray-500 ">
                            <button onClick={(()=>setButtonClicked(true))}><i className="fa-regular fa-heart text-5xl"></i></button> 
                          </div>
                        }
                        
                        
                      </div>
                      
                    </div>
              </div>
        ):""}

    </bases.Base1>
  )
}
