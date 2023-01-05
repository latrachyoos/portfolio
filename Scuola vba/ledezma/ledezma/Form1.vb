Public Class Form1
    Dim nmax As Integer = 1000
    Dim arraycls(nmax - 1) As String
    Dim arraynm(nmax - 1) As String
    Dim arraygo(nmax - 1) As Integer
    Dim fileclassi As String = "csvclassi.csv"
    Dim indicelst As Integer
    Dim n As Integer
    Function cercanome(ByVal alunno As String)
        Dim k As Integer
        Dim ver As Boolean = False
        Do While Not ver And k < n
            If Trim(LCase(arraynm(k))) = Trim(LCase(alunno)) Then
                ver = True
                indicelst = k
            End If
            k += 1
        Loop


        Return ver
    End Function
    Function cercacls(ByVal classe As String)
        Dim k As Integer
        Dim ver As Boolean = False
        Do While Not ver And k < cmbclasse.Items.Count
            If LCase(cmbclasse.Items.Item(k)) = LCase(classe) Then
                ver = True

            End If
            k += 1
        Loop


        Return ver
    End Function
    Sub visualizza()
        lstcls.Items.Clear()
        lstnm.Items.Clear()
        lstGa.Items.Clear()
        For k = 0 To n - 1
            lstcls.Items.Add(arraycls(k))
            lstnm.Items.Add(arraynm(k))
            lstGa.Items.Add(arraygo(k))
        Next

    End Sub
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        FileOpen(1, fileclassi, OpenMode.Input)
        Do While Not EOF(1)
            cmbclasse.Items.Add(UCase(LineInput(1)))
        Loop
        FileClose(1)
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BTNAGGCLS.Click
        If Trim(txtaggiungiclasse.Text) <> "" Then
            If Not cercacls(Trim(txtaggiungiclasse.Text)) Then
                FileOpen(2, fileclassi, OpenMode.Append)
                PrintLine(2, UCase(Trim(txtaggiungiclasse.Text)))
                cmbclasse.Items.Add(UCase(txtaggiungiclasse.Text))
                FileClose(2)


                MessageBox.Show("AGGIUNTO CORETTAMENTE")
            Else
                MessageBox.Show("CLASSE GIA' ESISTENTE NELL'ELENCO")
            End If
        Else
            MessageBox.Show("INSERISCI UNA CLASSE!")
        End If
        txtaggiungiclasse.Text = ""
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        If cmbclasse.SelectedIndex <> -1 And Trim(txtnome.Text) <> "" And IsNumeric(txtggassenza.Text) Then
            arraycls(n) = cmbclasse.SelectedItem
            arraynm(n) = txtnome.Text
            arraygo(n) = txtggassenza.Text
            n += 1
            txtnome.Text = ""
            txtggassenza.Text = ""
            cmbclasse.Text = "SELEZIONA CLASSE"
            visualizza()
            MessageBox.Show("DATI AGGIUNTI CORETTAMENTE")
        Else
            MessageBox.Show("INSERICI TUTTI I DATI CORETTAMENTE")
        End If
    End Sub

    Private Sub Button1_Click_1(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim max As Integer = arraygo(0)
        Dim indice As Integer
        For k = 1 To n - 1
            If arraygo(k) > max Then
                max = arraygo(k)
                indice = k
            End If
        Next
        lstcls.SelectedIndex = indice
        lstnm.SelectedIndex = indice
        lstGa.SelectedIndex = indice

    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        If lstGa.Items.Count > 1 Then
            Dim somma As Integer

            For k = 0 To n - 1
                somma += arraygo(k)
            Next
            MessageBox.Show((somma / (lstGa.Items.Count)))
        Else
            MessageBox.Show("DEVONO ESSERCI ALMENO DUE STUDENTI")
        End If

    End Sub

    
    Private Sub Button4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button4.Click
        If IsNumeric(txtgiorni.Text) Then

            If txtnomealunno.Text <> "" Then
                If cercanome(Trim(txtnomealunno.Text)) Then
                    If arraygo(indicelst) <= (txtgiorni.Text \ 2) Then
                        MessageBox.Show("L'ALUNNO NON SUPERA IL 50% DI GIORNI DI ASSENZA CONSENTITI IN UN ANNO")
                    Else
                        MessageBox.Show("L'ALUNNO SUPERA IL 50% DI GIORNI DI ASSENZA CONSENTITI IN UN ANNO")
                    End If
                Else
                    MessageBox.Show("NESSUN ALUNNO TROVATO")

                End If
                txtnomealunno.Text = ""
            Else
                MessageBox.Show("INSERISCI UN NOME VALIDO")

            End If

        Else
            MessageBox.Show("INSERISCI I GIORNI CORETTAMENTE")
        End If

    End Sub
End Class
