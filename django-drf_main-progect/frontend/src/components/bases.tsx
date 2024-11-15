import * as footers from "./footers";
import * as navbars from "./navbars";

export function Base1({ children }: any) {
  return (
    <main className={"m-0 p-0"}>
      <navbars.Navbar />
      <div className="children">
        {children}
      </div>
      <div><footers.Footer /></div>
    </main>
  );
}

