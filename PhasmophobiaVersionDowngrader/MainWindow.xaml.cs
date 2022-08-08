using Microsoft.UI;
using Microsoft.UI.Windowing;
using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;
using Microsoft.UI.Xaml.Controls.Primitives;
using Microsoft.UI.Xaml.Data;
using Microsoft.UI.Xaml.Input;
using Microsoft.UI.Xaml.Media;
using Microsoft.UI.Xaml.Navigation;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Foundation;
using Windows.Foundation.Collections;


namespace PhasmophobiaVersionDowngrader
{
    public sealed partial class MainWindow : Window
    {
        List<UpdateListJson> datos = new List<UpdateListJson>();
        private string selectedManifest = null;
        private Process proc;
        private bool loginTry = false;

        public MainWindow()
        {
            this.InitializeComponent();
            Title = "Phasmophobia Version Downgrader";
            SetWindowSize();
            SetUpdateList();
        }

        public void SetWindowSize()
        {
            IntPtr hWnd = WinRT.Interop.WindowNative.GetWindowHandle(this); // m_window in App.cs
            WindowId windowId = Win32Interop.GetWindowIdFromWindow(hWnd);
            AppWindow appWindow = AppWindow.GetFromWindowId(windowId);

            var size = new Windows.Graphics.SizeInt32();
            size.Width = 672;
            size.Height = 537;
            appWindow.Resize(size);
        }


        private void SetUpdateList()
        {
            var url = "https://raw.githubusercontent.com/DaniGP17/PhasmoVersionChanger/main/manifest.json";

            var httpRequest = (HttpWebRequest)WebRequest.Create(url);


            var httpResponse = (HttpWebResponse)httpRequest.GetResponse();
            using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
            {
                var result = streamReader.ReadToEnd();
                List<UpdateListJson> todo = JsonConvert.DeserializeObject<List<UpdateListJson>>(result);

                foreach (var item in todo)
                {
                    UpdatesList.Items.Add(item.date.Substring(0, item.date.Length - 10));
                    datos.Add(new UpdateListJson { date = item.date, manifest = item.manifest, mono = item.mono });
                }
            }
        }

        private void UpdatesList_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            foreach (var i in datos)
            {
                if (i.date.Substring(0, i.date.Length - 10) == UpdatesList.SelectedItem.ToString())
                {
                    versionDate.Text = "Version Date: " + i.date;
                    betaVersion.Text = "Beta Version: False";
                    manifest.Text = "Manifest: " + i.manifest;
                    selectedManifest = i.manifest;
                    if (i.mono == "false")
                    {
                        gameAssembly.Text = "Game Assembly: IL2CPP";
                        return;
                    }
                    gameAssembly.Text = "Game Assembly: JET Mono";
                }
            }
        }

        private void SelectVersion_Click(object sender, RoutedEventArgs e)
        {
            if(UpdatesList.SelectedIndex == -1)
            {
                return;
            }
            SelectVersionPanel.Visibility = Visibility.Collapsed;
            LoginSteamPanel.Visibility = Visibility.Visible;
            //FinishPanel.Visibility = Visibility.Visible;
        }

        private void LoginButton_Click(object sender, RoutedEventArgs e)
        {
            LoadingBarLoginSteam.Visibility = Visibility.Visible;
            LoginButton.IsEnabled = false;

            var username = steamUsername.Text;
            var password = steamPassword.Password;

            if (string.IsNullOrEmpty(username) || string.IsNullOrEmpty(password))
            {
                LoginButton.IsEnabled = true;
                ErrorLoginSteam.IsOpen = true;
                ErrorLoginSteam.Message = "The username and password fields are empty, please complete it.";
                LoadingBarLoginSteam.Visibility = Visibility.Collapsed;
                return;
            }

            if (!loginTry)
            {
                loginTry = true;
                proc = Process.Start(new ProcessStartInfo(@"C:\Users\danie\source\repos\PhasmophobiaVersionDowngrader\PhasmophobiaVersionDowngrader\Depot\DepotDownloader.exe")
                {
                    Arguments = "-app 739630 -depot 739631 -manifest " + selectedManifest + " -username " + username + " -password " + password,
                    WindowStyle = ProcessWindowStyle.Normal,
                    CreateNoWindow = true,
                    UseShellExecute = false,
                    RedirectStandardError = true,
                    RedirectStandardOutput = true,
                    RedirectStandardInput = true
                });

                while (!proc.StandardOutput.EndOfStream)
                {
                    string line = proc.StandardOutput.ReadLine();
                    if (line.Contains("protected"))
                    {
                        System.Diagnostics.Debug.WriteLine("Esta protegido por steam guard");
                        LoginSteamPanel.Visibility = Visibility.Collapsed;
                        AuthCodeSteamPanel.Visibility = Visibility.Visible;
                    }
                    else if (line.Contains("InvalidPassword"))
                    {
                        ErrorLoginSteam.IsOpen = true;
                        ErrorLoginSteam.Message = "Invalid password, please try again.";
                        LoadingBarLoginSteam.Visibility = Visibility.Collapsed;
                        LoginButton.IsEnabled = true;
                    }
                    else if (line.Contains("RateLimitExceeded"))
                    {
                        ErrorLoginSteam.IsOpen = true;
                        ErrorLoginSteam.Message = "Your IP has been rate limited due to the request exceeded, wait and try again.";
                        LoadingBarLoginSteam.Visibility = Visibility.Collapsed;
                        LoginButton.IsEnabled = true;
                    }
                    else if (line.Contains("Got session token!"))
                    {
                        AuthCodeSteamPanel.Visibility = Visibility.Collapsed;
                        DownloadPanel.Visibility = Visibility.Visible;
                    }
                    else if (line.Contains("% depots"))
                    {
                        var porcentage = line.Substring(1, 7);
                        DownloadPorcentage.Text = "Downloading: " + porcentage;
                    }
                    else if (line.Contains("Total downloaded"))
                    {
                        DownloadPorcentage.Text = "Downloading: 100%";
                    }
                    System.Diagnostics.Debug.WriteLine(line);
                }
            }
        }

        private void AuthButton_Click(object sender, RoutedEventArgs e)
        {
            var authCode = AuthCode.Text;
            if (string.IsNullOrEmpty(authCode))
            {
                AuthCodeLoginError.IsOpen = true;
                AuthCodeLoginError.Message = "The auth code field is empty, please complete it.";
                return;
            }

            proc.StandardInput.WriteLine(authCode);

            AuthCodeSteamPanel.Visibility = Visibility.Collapsed;
            DownloadPanel.Visibility = Visibility.Visible;
        }

        private void CancelDownload_Click(object sender, RoutedEventArgs e)
        {
            DownloadPanel.Visibility = Visibility.Collapsed;
            SelectVersionPanel.Visibility = Visibility.Visible;
        }

        private void BackToSelect_Click(object sender, RoutedEventArgs e)
        {
            FinishPanel.Visibility = Visibility.Collapsed;
            SelectVersionPanel.Visibility = Visibility.Visible;
        }
    }

    class UpdateListJson
    {
        public string date { get; set; }
        public string manifest { get; set; }
        public string mono { get; set; }
    }
}
