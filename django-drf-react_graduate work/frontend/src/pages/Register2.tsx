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
  const userRegister2 = useSelector((state: any) => state.userRegister2);
  const username = utils.LocalStorage.get('username')
  const [form, setForm] = useState({
    username: "",
    name: "",
    surname: "",
    number: "",
    avatar: null
  });

  function sendForm(event: any) {
    event.preventDefault();

    if (!userRegister2.load) {
      const formData = new FormData();
      formData.append('username', username);
      formData.append('name', form.name);
      formData.append('surname', form.surname);
      formData.append('number', form.number);
      //@ts-ignore
      formData.append('avatar', form.avatar);
      
      components.constructorWebAction(
        dispatch,
        constants.userRegister2,
        `http://127.0.0.1:8000/api/register2`,
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

  // TODO useEffect //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  useEffect(() => {
    if (userRegister2 && userRegister2.data) {
      setTimeout(() => {
        navigate("/login");
        dispatch({ type: constants.userRegister2.reset });
      }, 2000);
    }
  }, [userRegister2]);

  useEffect(() => {
    if (constants.isDebug) {
      console.log("userRegister2: ", userRegister2);
    }
  }, [userRegister2]);
  return (
    <bases.Base1>
      <div className="sm:mx-auto sm:w-full sm:max-w-sm mt-20">
            <h2 className="mt-10 text-center text-3xl font-bold leading-9 tracking-tight text-slate-50">Введите данные для регистрации</h2>
            </div>
            <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
              <form className={""} onSubmit={sendForm}>
                  <div>
                      <label htmlFor="email" className="block text-sm font-semibold leading-6 text-slate-50">Имя: </label>
                      <div className="mt-2">
                          <input onChange={(event) => setForm({ ...form, name: event.target.value })}  placeholder="Имя" type="text" required className="block w-full rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-slate-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-s sm:leading-6 p-2"/>
                      </div>
                  </div>

                  <div>
                      <label htmlFor="password" className="block text-sm font-semibold leading-6 text-slate-50">Фамилия:</label>
                      <div className="mt-2">
                          <input id="password" onChange={(event) => setForm({ ...form, surname: event.target.value })} placeholder="Фамилия" name="password" type="text" required className="block w-full rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-slate-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-s sm:leading-6 p-2"/>
                      </div>
                  </div>
                  
                  <div>
                      <label htmlFor="password" className="block text-sm font-semibold leading-6 text-slate-50">Номер:</label>
                      <div className="mt-2">
                          <input id="password2" onChange={(event) => setForm({ ...form, number: event.target.value })} placeholder="Номер телефона"  name="password" type="text" required className="block w-full rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-slate-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-s sm:leading-6 p-2"/>
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
                        required
                      />
                    </div>
                  </div>
                  
                  <article>
                    <loaders.Loader1 isView={userRegister2.load} />
                    {userRegister2.error && (
                      <div className="alert alert-danger" role="alert">
                        {userRegister2.error}
                      </div>
                    )}
                    {userRegister2.fail && (
                      <div className="alert alert-danger" role="alert">
                        {userRegister2.fail}
                      </div>
                    )}
                    {userRegister2.data && (
                      <div className="alert alert-success" role="alert">
                        Данные успешно получены
                      </div>
                    )}
                  </article>
                  <div className="mt-10">
                      <button type="submit" className="flex w-full justify-center rounded-md bg-yellow-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-yellow-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 ">Зарегистрироваться</button>
                  </div>
              </form>
            </div>
    </bases.Base1>
  );
}
