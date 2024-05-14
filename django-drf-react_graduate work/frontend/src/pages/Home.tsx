// TODO external  //////////////////////////////////////////////////////////////////
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
// TODO internal //////////////////////////////////////////////////////////////////
import * as bases from "../components/bases";
import * as components from "../components/components";
import * as constants from "../components/constants";
import * as store from "../components/store";
import * as loaders from "../components/loaders";


export default function Page() {
  const dispatch = useDispatch();
  const category = useSelector((state: any) => state.categoryList);
  const [data,SetData] = useState([])

  async function getCategory() {
    if (!category.load) {
      components.constructorWebAction(
        dispatch,
        constants.categoryList,
        `http://127.0.0.1:8000/api/category`,
        "GET",
      );
    }
  }
  useEffect(() => {
    getCategory();
  }, []);

  useEffect(() => {
    if (category.data) {
      const newArray: any = [];
      for (let i = 0; i < category.data.length; i += 1) {
          newArray.push(category.data[i]);
      }
      SetData(newArray);
    }
  }, [category.data]);



  return (
    <bases.Base1>
      <div className="flex items-center flex-col gap-y-10 mx-80 mt-20">
        <h3 className="text-4xl font-bold leading-9 tracking-tight text-slate-50">Категории:</h3>
        <div className=" columns-2 ">
            {!category.load ? data.map((item:any,index:number=3) => (
              <div key = {item.id} className="rounded text-slate-800 mt-10 mr-10">
                <Link to ={`/category/${item.slug}`} className= {`category flex flex-col items-center bg-white rounded  w-96 h-44 `} >
                  <img src={`static${item.image}`} alt="" className="w-96 rounded h-36"/>
                  <span className="text-slate-900 text-lg font-bold pl-2">{item.title}</span>
                </Link>
              </div>

            
            )): ""}
            </div>
        </div>
    </bases.Base1>
  );
}
