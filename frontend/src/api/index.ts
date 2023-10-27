import { dataURItoBlob } from '@/helpers';

export const predictNumber = async (
    dataURL: any
): Promise<{ prediction: number }> => {
    if (!dataURL) {
        throw new Error('No dataURL provided');
    }

    let formData = new FormData();
    formData.append('file', dataURItoBlob(dataURL));

    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/predict`, {
        method: 'POST',
        body: formData,
    });
    return response.json();
};
