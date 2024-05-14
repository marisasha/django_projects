// external
import { BrowserRouter, Routes, Route } from "react-router-dom";

// base
import Home from "../pages/Home";
import Login from "../pages/Login";
import Logout from "../pages/Logout";
import Register from "../pages/Register";
import Register2 from "../pages/Register2";

// book
import StartapList from "../pages/StartapList";
import StartapDetail from "../pages/StartapDetail";
import StartapCreate from "../pages/StartapCreate";
import Profile from "../pages/Profile";

// notes


export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        {/* base */}
        <Route path={""} element={<Home />}></Route>
        <Route path={"register/"} element={<Register />}></Route>
        <Route path={"register2/"} element={<Register2 />}></Route>
        <Route path={"login/"} element={<Login />}></Route>
        <Route path={"logout/"} element={<Logout />}></Route>

        {/* book */}
        <Route path={"category/:slug"} element={<StartapList />}></Route>
        <Route path={"profile/"} element={<Profile />}></Route>
        <Route path={"category/:slug/:id"} element={<StartapDetail />}></Route>
        <Route path={"create/"} element={<StartapCreate />}></Route>

        {/* safe redirect */}
        <Route path={"*"} element={<Home />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
