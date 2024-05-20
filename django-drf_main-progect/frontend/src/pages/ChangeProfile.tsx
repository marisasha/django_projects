// external
import { useEffect, useRef, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";

// internal
import * as bases from "../components/bases";
import * as utils from "../components/utils";
import * as constants from "../components/constants";
import * as components from "../components/components";
import * as loaders from "../components/loaders";

export default function Page() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const userUpdate = useSelector((state: any) => state.userUpdate);
  const username = utils.LocalStorage.get('username')
  const [form, setForm] = useState({
    username: "",
    name: "",
    surname: "",
    number: "",
    status:"Начинающий предприниматель",
    avatar: null
  });

  function sendForm(event: any) {
    event.preventDefault();

    if (!userUpdate.load) {
      console.log(form)
      const formData = new FormData();
      formData.append('username', username);
      formData.append('name', form.name);
      formData.append('surname', form.surname);
      formData.append('number', form.number);
      formData.append('status', form.status);
      //@ts-ignore
      formData.append('avatar', form.avatar);
      
      components.constructorWebAction(
        dispatch,
        constants.userUpdate,
        `${constants.host}/api/change/profile`,
        "POST",
        formData,
        10000,
        true,
      );
    } 
  }

  const handleAvatarChange = (event:any) => {
    const file = event.target.files[0];
    setForm({ ...form, avatar: file });
    console.log(form.avatar)
  };
  const handleStatusChange = (event:any) => {
    const status  = event.target.value;
    setForm({ ...form, status: status });
    
};

  // TODO useEffect //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  useEffect(() => {
    if (userUpdate && userUpdate.data) {
      setTimeout(() => {
        navigate("/profile");
        dispatch({ type: constants.userUpdate.reset });
      }, 2000);
    }
  }, [userUpdate]);

  useEffect(() => {
    if (constants.isDebug) {
      console.log("userUpdate: ", userUpdate);
    }
  }, [userUpdate]);
  return (
    <bases.Base1>
      <div className="sm:mx-auto sm:w-full sm:max-w-sm mt-20">
            <h2 className="mt-10 text-center text-3xl font-bold leading-9 tracking-tight text-slate-50">Введите данные , которые хотите изменить</h2>
            </div>
            <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
              <form className={""} onSubmit={sendForm}>
                  <div>
                      <label className="block text-sm font-semibold leading-6 text-slate-50">Имя: </label>
                      <div className="mt-2">
                          <input onChange={(event) => setForm({ ...form, name: event.target.value })}  placeholder="Имя" type="text" className="block w-full rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-slate-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-s sm:leading-6 p-2"/>
                      </div>
                  </div>

                  <div>
                      <label htmlFor="password" className="block text-sm font-semibold leading-6 text-slate-50">Фамилия:</label>
                      <div className="mt-2">
                          <input id="password" onChange={(event) => setForm({ ...form, surname: event.target.value })} placeholder="Фамилия" name="password" type="text" className="block w-full rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-slate-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-s sm:leading-6 p-2"/>
                      </div>
                  </div>
                  
                  <div>
                      <label htmlFor="password" className="block text-sm font-semibold leading-6 text-slate-50">Номер:</label>
                      <div className="mt-2">
                          <input id="password2" onChange={(event) => setForm({ ...form, number: event.target.value })} placeholder="Номер телефона"  name="password" type="text" className="block w-full rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-slate-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-s sm:leading-6 p-2"/>
                      </div>
                  </div>
                  <div>
                    <label htmlFor="avatar" className="block text-sm font-semibold leading-6 text-slate-50">Аватар:</label>
                    <div className="mt-2">
                      <input
                        type="file"
                        name="avatar"
                        className="form-control form-control-m"
                        onChange={handleAvatarChange}
                        accept=".png, .jpg, .jpeg"

                      />
                    </div>
                  </div>
                  <div>
                      <label className="block text-sm font-semibold leading-6 text-slate-50">Ваш статус: </label>
                      <select onChange={handleStatusChange} className="block w-96 rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-gray-300 ext-slate-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-s sm:leading-6 p-2">
                            <option value="Начинающий предприниматель">Начинающий предприниматель</option>
                            <option value="Предпринимаатель с опытом">Предприниматель с опытом</option>
                            <option value="Бизнесмен">Бизнесмен</option>
                            <option value="Инвестор">Инвестор</option>
                      </select>
                  </div>
                  <article>
                    <loaders.Loader1 isView={userUpdate.load} />
                    {userUpdate.error && (
                      <div className="alert alert-danger" role="alert">
                        {userUpdate.error}
                      </div>
                    )}
                    {userUpdate.fail && (
                      <div className="alert alert-danger" role="alert">
                        {userUpdate.fail}
                      </div>
                    )}
                    {userUpdate.data && (
                      <div className="w-full h-12 bg-green-500 text-slate-50  text-bold text-m rounded mt-3 flex items-center justify-center font-semibold" role="alert">
                        Данные успешно изменены !
                      </div>
                    )}
                  </article>
                  <div className="mt-10">
                      <button type="submit" className="flex w-full justify-center rounded-md bg-yellow-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-yellow-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 ">Изменить</button>
                  </div>
              </form>
            </div>
    </bases.Base1>
  );
}
