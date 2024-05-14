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

export default function Page() {
  // TODO hooks //////////////////////////////////////////////////////////////////
  const dispatch = useDispatch();
  const startaps = useSelector((state: any) => state.startapList);
  const [data, setData] = useState([]);
  const [isReversed, setIsReversed] = useState(false);
  const params = useParams()

  // TODO functions //////////////////////////////////////////////////////////////////
  async function getStartaps() {
    if (!startaps.load) {
      //  && !startaps.data
      components.constructorWebAction(
        dispatch,
        constants.startapList,
        `http://127.0.0.1:8000/api/${params.slug}`,
        "GET",
      );
    }
  }

  // TODO useEffect //////////////////////////////////////////////////////////////////
  useEffect(() => {
    getStartaps();
  }, []);

  useEffect(() => {
    if (startaps.data) {
      //[1, 2, 3] -> [3, 2, 1]
      const newArray: any = [];
      for (let i = 0; i < startaps.data.length; i += 1) {
        if (isReversed) {
          newArray.push(startaps.data[startaps.data.length - i - 1]);
        } else {
          newArray.push(startaps.data[i]);
        }
      }
      setData(newArray);
    }
  }, [startaps.data, isReversed]);

  useEffect(() => {
    console.log("startaps: ", startaps);
  }, [startaps]);

  return (
    <bases.Base1>
      {/* <hr className={"mt-5"} />
      <div className={"d-flex container justify-content-end"}>
        {isReversed ? (
          <button
            className={"btn btn-primary m-1 p-3"}
            onClick={() => {
              setIsReversed(!isReversed);
            }}
          >
            обратная сортировка
          </button>
        ) : (
          <button
            className={"btn btn-outline-primary m-1 p-3"}
            onClick={() => {
              setIsReversed(!isReversed);
            }}
          >
            прямая сортировка
          </button>
        )}
      </div> */}
      <div className="flex flex-col gap-y-10 mx-80 mt-20">
        <h3 className="text-4xl font-bold leading-9 tracking-tight text-slate-50">Проекты в этой категории:</h3>
        <loaders.Loader1 isView={startaps.load} />
          {startaps.error && (
            <div className="alert alert-danger" role="alert">
              {startaps.error}
            </div>
          )}
          {startaps.fail && (
            <div className="alert alert-danger" role="alert">
              {startaps.fail}
            </div>
          )}
        <div className="flex flex-col gap-y-5">
          {!startaps.load && data && data.length > 0
            ? data.map((item: any, index: number) => (
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
                      <div>
                        <span className="text-slate-900 text-lg font-bold "> Отметок нравится : {item.likes_count} </span>
                      </div>
                    </div>
                  </Link>
                  </div>
                ))
                : ""}
        </div>
      </div>



      </bases.Base1>
  );
}
