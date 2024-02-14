import classNames from "classnames"
import { useRef } from "react"
import { InputCheckboxComponent } from "./types"

export const InputCheckbox: InputCheckboxComponent = ({ id, checked = false, disabled, onChange }) => {
  const { current: inputId } = useRef(`KaizntreeInputCheckbox-${id}`)

  return (
    <div className="KaizntreeInputCheckbox--container" data-testid={inputId} >
      <label
        className={classNames("KaizntreeInputCheckbox--label", {
          "KaizntreeInputCheckbox--label-checked": checked,
          "KaizntreeInputCheckbox--label-disabled": disabled,
        })}
       htmlFor={inputId} // fix for bug 2
      />
      <input
        id={inputId}
        type="checkbox"
        className="KaizntreeInputCheckbox--input"
        checked={checked}
        disabled={disabled}  
        onChange={() => {
          onChange(!checked)
        }}
        onClick={()=>console.log("clicked by index")}
      />
    </div>
  )
}
