// external
import { useEffect, useState } from "react";
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
    const startapCreate = useSelector((state: any) => state.startapCreate);
    const username = utils.LocalStorage.get('username')
    const [form, setForm] = useState({
        username: username,
        category: 10,
        title: "",
        description: "",
        location: "",
        deposit_amount: 0,
        image : null,
        pdf : null,
        file : null


    });
    const category = useSelector((state: any) => state.categoryList);
    const [data,SetData] = useState([])
    
    async function getCategory() {
        if (!category.load) {
            components.constructorWebAction(
                dispatch,
                constants.categoryList,
                `${constants.host}/api/category`,
                "GET",
            );
            }
        }
        

    function sendForm(event: any) {
        event.preventDefault();
        console.log(form)

        if (!startapCreate.load) {
        const formData = new FormData();
        formData.append('username', form.username);
        //@ts-ignore
        formData.append('category', form.category);
        formData.append('title', form.title);
        formData.append('description', form.description);
        formData.append('location', form.location);
        //@ts-ignore
        formData.append('deposit_amount', form.deposit_amount);
        //@ts-ignore
        formData.append('image', form.image);
        //@ts-ignore
        formData.append('pdf', form.pdf);
        //@ts-ignore
        formData.append('file', form.file);
        
        components.constructorWebAction(
            dispatch,
            constants.startapCreate,
            `${constants.host}/api/create-startap`,
            "POST",
            formData,
            10000,
            true,
        );
        } 
    }
    const handleCategoryChange = (event:any) => {
        const category  = event.target.value;
        setForm({ ...form, category: category });
        
    };
    const handleAvatarChange = (event:any) => {
        const file = event.target.files[0];
        setForm({ ...form, image: file });
    };
    const handlePDFChange = (event:any) => {
        const file = event.target.files[0];
        setForm({ ...form, pdf: file });
    };
    const handleFileChange = (event:any) => {
        const file = event.target.files[0];
        setForm({ ...form, file: file });
    };

    // TODO useEffect //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    useEffect(() => {
        if (startapCreate && startapCreate.data) {
            utils.LocalStorage.set("username", form.username);
            setTimeout(() => {
                navigate("/");
                dispatch({ type: constants.startapCreate.reset });
            }, 2000);
        }
    }, [startapCreate]);

    useEffect(() => {
        if (constants.isDebug) {
        console.log("startapCreate: ", startapCreate);
        }
    }, [startapCreate]);

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
            <div className="flex flex-col gap-y-10 mx-20 mt-20 pt-10 rounded-lg items-center box-border">
                <h3 className="text-4xl font-bold leading-9 tracking-tight text-slate-50 m-auto">Создание проекта :</h3>
                    <form className={""} onSubmit={sendForm}>
                        <div className="flex gap-x-2">
                            <div>
                                <label className="block text-sm font-semibold leading-6 text-slate-50 ">Название: </label>
                                <div className="mt-2">
                                    <input onChange={(event) => setForm({ ...form, title: event.target.value })}   type="text" required placeholder="..." className="block w-96 rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-gray-300 ext-slate-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-s sm:leading-6 p-2"/>
                                </div>
                            </div>

                            <div>
                                <label  className="block text-sm font-semibold leading-6 text-slate-50 ">Описание:</label>
                                <div className="mt-2">
                                    <input onChange={(event) => setForm({ ...form, description: event.target.value })}  name="password" type="text" required placeholder="..." className="block w-96 rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-gray-300 ext-slate-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-s sm:leading-6 p-2"/>
                                </div>
                            </div>
                        </div>
                        
                        <div className="flex gap-x-2">
                            <div>
                                <label className="block text-sm font-semibold leading-6 text-slate-50 ">Локация проекта: </label>
                                <div className="mt-2">
                                    <input onChange={(event) => setForm({ ...form, location: event.target.value })}  type="text" required placeholder="..." className="block w-96 rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-gray-300 ext-slate-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-s sm:leading-6 p-2"/>
                                </div>
                            </div>

                            <div>
                                <label  className="block text-sm font-semibold leading-6 text-slate-50 ">Необходимая сумма вложения:</label>
                                <div className="mt-2">
                                    {/* @ts-ignore */}
                                    <input onChange={(event) => setForm({ ...form, deposit_amount: event.target.value })}  name="password" type="number" required placeholder="..." className="block w-96 rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-gray-300 ext-slate-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-s sm:leading-6 p-2"/>
                                </div>
                            </div>
                        </div>

                        <div className="flex gap-x-2">
                            <div>
                                <label className="w-96 block text-sm font-semibold leading-6 text-slate-50">Категория:</label>
                                <select onChange={handleCategoryChange} className="block w-96 rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-gray-300 ext-slate-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-s sm:leading-6 p-2">
                                    {!category.load ? data.map((item:any, index:number) => (
                                        <option key={index} value={item.id}>{item.title}</option>
                                    )) : ""}
                                </select>
                            </div>
                            <div>
                                    <label htmlFor="pdf" className="w-96 block text-sm font-semibold leading-6 text-slate-50">PDF-презентация проекта:</label>
                                    <div>
                                    <input
                                        type="file"
                                        name="pdf"
                                        className="form-control form-control-m"
                                        onChange={handlePDFChange}
                                        accept=".pdf"
                                    />
                                    </div>
                                </div>
                        </div>
                        
                        <div className="flex gap-x-2">
                            <div>
                                <label htmlFor="avatar" className="w-96 block text-sm font-semibold leading-6 text-slate-50">Изображение:</label>
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
                                <label htmlFor="file" className="w-96 block text-sm font-semibold leading-6 text-slate-50">Файлы проекты:</label>
                                <div className="mt-2">
                                    <input
                                        type="file"
                                        name="file"
                                        className="form-control form-control-m"
                                        onChange={handleFileChange}
                                        required
                                    />
                                </div>
                            </div>
                        </div>
                        
                        <article>
                        <loaders.Loader1 isView={startapCreate.load} />
                            {startapCreate.error && (
                            <div className="alert alert-danger" role="alert">
                                {startapCreate.error}
                            </div>
                            )}
                            {startapCreate.fail && (
                            <div className="alert alert-danger" role="alert">
                                {startapCreate.fail}
                            </div>
                            )}
                            {startapCreate.data && (
                            <div className="w-full h-12 bg-green-500 text-slate-50  text-bold text-m rounded mt-3 flex items-center justify-center font-semibold" role="alert">
                                Проект успешно опубликован !
                            </div>
                            )}
                        </article>

                        <div className="mt-3 m-auto flex justify-center">
                            <button type="submit" className="flex w-60 justify-center rounded-md bg-yellow-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-yellow-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 ">Опубликовать проект</button>
                        </div>
                        </form>
                    </div>
                
        </bases.Base1>
    )
}