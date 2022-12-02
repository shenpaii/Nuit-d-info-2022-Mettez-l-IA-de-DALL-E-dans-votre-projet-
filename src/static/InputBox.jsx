import React from 'react';

export const InputBox = ({label, setAttribute}) => {
  return (
    <div className="label-input-pair">
        <label className="label">{label}</label>
        <input
        className="main-input" 
        onChang={(e) => setAttribute(e.target.value)}
         />
      </div>
    
  );
};
