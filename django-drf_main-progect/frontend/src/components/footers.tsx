import * as constants from "../components/constants";

export function Footer() {
  return (
    <nav className="flex flex-row-reverse items-center m-0 bg-yellow-500 w-full h-28 px-10" aria-label="Global">
        <div className="flex flex-col ">
          <span className="text-sm font-semibold leading-6 text-slate-50 hover:text-gray-600"> Автор: @marisasha </span>
          <span className="text-sm font-semibold leading-6 text-slate-50 hover:text-gray-600"> 2024 год</span>
          <span className="text-sm font-semibold leading-6 text-slate-50 hover:text-gray-600"> по вопросам : <a href="https://web.telegram.org/a/#881596032" className="text-purple-900 hover:text-purple-500">*тык*</a></span>
          <a href={`${constants.host}comments/`} className="text-sm font-semibold leading-6 text-slate-50 hover:text-gray-600">Оставьте отзыв нашему сайту</a>
        </div>
      </nav>
  );
}

export function Footer2() {
  return <footer></footer>;
}
