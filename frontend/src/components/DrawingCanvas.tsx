'use client';

import { predictNumber } from '@/api';
import React, { useRef, useState } from 'react';
import CanvasDraw, { CanvasDrawProps } from 'react-canvas-draw';

type Response = {
    prediction: number;
};

const DrawingCanvas: React.FC = () => {
    const [response, setResponse] = useState<Response | null>(null);
    const canvasRef = useRef<any>(null);

    const handleSendDrawing = async () => {
        if (canvasRef.current) {
            const dataURL =
                canvasRef.current.canvas.drawing.toDataURL('image/png');
            try {
                const data = await predictNumber(dataURL);
                setResponse(data);
                console.log(data);
                handleResetDrawing();
            } catch (error) {
                console.error("Erreur lors de l'envoi de l'image:", error);
            }
        }
    };

    const handleResetDrawing = () => {
        if (canvasRef.current) {
            canvasRef.current.clear();
        }
    };

    const canvasOptions: CanvasDrawProps = {
        lazyRadius: 0,
        brushRadius: 5,
        canvasHeight: 320,
        canvasWidth: 320,
        brushColor: '#000',
    };

    return (
        <div className="flex flex-col justify-center items-center gap-3 mb-4">
            <div
                className="flex flex-col justify-center items-center
            "
            >
                <h1 className="text-2xl font-bold mb-2">Dessinez un chiffre</h1>
                <h2 className="text-lg">
                    Prédiction :&nbsp;
                    <span className="font-semibold">
                        {response ? response.prediction : '?'}
                    </span>
                </h2>
            </div>
            <CanvasDraw ref={canvasRef} {...canvasOptions} />
            <div className="flex w-full justify-between">
                <button
                    onClick={handleResetDrawing}
                    className="bg-gray-400 text-white p-2 rounded"
                >
                    Effacer
                </button>
                <button
                    onClick={handleSendDrawing}
                    className="bg-blue-500 text-white p-2 rounded"
                >
                    Prédire
                </button>
            </div>
        </div>
    );
};

export default DrawingCanvas;
