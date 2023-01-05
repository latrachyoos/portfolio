Public Class Form1
    Const nomefile As String = "rubrica.csv"
    Dim indiceSel As Integer = -1
    Dim R As Integer
    Dim NC As Integer = 5
    Sub Azzera()
        'procedura di svuotamento delle caselle di testo
        'txtCognome.Clear()
        'txtCittà.Clear()
        'txtIndirizzo.Clear()
        'txtNome.Clear()
        'txtTelefono.Clear()
        '..........
        For Each txt As TextBox In Panel1.Controls
            txt.Text = ""
        Next
        txtCognome.Select()
        'reset della variabile IndiceSel
        indiceSel = -1
        'ricordiamo che il valore -1 indica che non c'è alcun record selezionato
    End Sub

    Sub carica()
        Dim s As String
        FileOpen(1, nomefile, OpenMode.Output)
        For i = 0 To R - 1
            s = ""
            'dgv.Rows.Add()
            For k = 0 To NC - 1
                s &= dgv.Rows(i).Cells(k).Value & ";"
            Next
            PrintLine(1, s)
        Next

        FileClose(1)

    End Sub

    Sub prendi()
        Dim s() As String
        R = 0
        FileOpen(1, nomefile, OpenMode.Input)
        Do While Not EOF(1)
            s = Split(LineInput(1), ";")
            dgv.Rows.Add()
            For i = 0 To NC - 1
                dgv.Rows(R).Cells(i).Value = s(i)
            Next
            R += 1
        Loop
        FileClose(1)
    End Sub

    Private Sub btnSalvaInDgv_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnSalvaInDgv.Click
        Timer1.Stop()
        Dim c As Integer = 0
        Dim cont As Boolean = True
        For Each txt As TextBox In Panel1.Controls
            If txt.Text = "" Then
                cont = False
            End If
        Next
        If indiceSel < 0 And cont Then 'indica che non si tratta di una modifica dei dati
            'aggiunge nella dgv 
            dgv.Rows.Add()
            dgv.Rows(R).Cells("Cognome").Value = txtCognome.Text
            dgv.Rows(R).Cells("Nome").Value = txtNome.Text
            dgv.Rows(R).Cells("Telefono").Value = txtTelefono.Text
            dgv.Rows(R).Cells("Indirizzo").Value = txtIndirizzo.Text
            dgv.Rows(R).Cells("Città").Value = txtCittà.Text
            R += 1
        ElseIf indiceSel > -1 And cont Then
            'sostituisce i dati presenti nella riga selezionata con i dati modificati dall'utente 
            'la riga da sostituire viene intercettata grazie al valore presente nella variabile indiceSel
            dgv.Rows(indiceSel).Cells("Cognome").Value = txtCognome.Text
            dgv.Rows(indiceSel).Cells("Nome").Value = txtNome.Text
            dgv.Rows(indiceSel).Cells("Telefono").Value = txtTelefono.Text
            dgv.Rows(indiceSel).Cells("Indirizzo").Value = txtIndirizzo.Text
            dgv.Rows(indiceSel).Cells("Città").Value = txtCittà.Text
            'al termine dello spostamento le caselle di testo devono essere svuotate e la variabile indiceSel settata a -1
            'a tale scopo implementare la procedura Azzera
        End If
        Azzera()
    End Sub


    Private Sub dgv_CellDoubleClick(ByVal sender As Object, ByVal e As System.Windows.Forms.DataGridViewCellEventArgs) Handles dgv.CellDoubleClick
        'doppio click su una cella di una riga
        'carica tutti i valori della riga nelle caselle di testo
        txtCognome.Text = dgv.CurrentRow.Cells("Cognome").Value
        txtNome.Text = dgv.CurrentRow.Cells("Nome").Value
        txtTelefono.Text = dgv.CurrentRow.Cells("Telefono").Value
        txtIndirizzo.Text = dgv.CurrentRow.Cells("Indirizzo").Value
        txtCittà.Text = dgv.CurrentRow.Cells("Città").Value
        'La variabile indiceSel contiene l'indice della riga selezionata, 
        'in modo che in futuro il valore possa essere utilizzato per inserire nella stessa
        'riga i valori modificati attraverso il ricorso alle caselle di testo
        indiceSel = dgv.CurrentRow.Index

    End Sub

    Private Sub btnSalvaInCSV_Click_1(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnSalvaInCSV.Click
        'SALVA TUTTI I DATI PRESENTI NELLA DGV IN UN FILE CSV 
        '(sostituisce tutti i dati presenti nel file)
        carica()
    End Sub

   

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        'All'avvio del programma caricare tutti i dati presenti nel file CSV all'interno della dataGridView
        'Dim s() As String
        'FileOpen(1, nomefile, OpenMode.Input)
        'Do While Not EOF(1)
        '    s = Split(LineInput(1), ";")
        '    dgv.Rows.Add()
        '    For i = 0 To NC - 1
        '        dgv.Rows(R).Cells(i).Value = s(i)
        '    Next
        '    R += 1
        'Loop

        'FileClose(1)
        prendi()
    End Sub


    Private Sub btnChiudi_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnChiudi.Click
        End
    End Sub

    Private Sub btncanc_Click(sender As System.Object, e As System.EventArgs) Handles btncanc.Click
        Dim ind As Integer
        ind = dgv.CurrentCell.RowIndex
        If ind > -1 And ind <> R - 1 Then
            dgv.Rows(ind).Cells("Cognome").Value = dgv.Rows(ind + 1).Cells("Cognome").Value
            dgv.Rows(ind).Cells("Nome").Value = dgv.Rows(ind + 1).Cells("Nome").Value
            dgv.Rows(ind).Cells("Telefono").Value = dgv.Rows(ind + 1).Cells("Telefono").Value
            dgv.Rows(ind).Cells("Indirizzo").Value = dgv.Rows(ind + 1).Cells("Indirizzo").Value
            dgv.Rows(ind).Cells("Città").Value = dgv.Rows(ind + 1).Cells("Città").Value
        Else
            dgv.Rows(R - 1).Cells("Cognome").Value = ""
            dgv.Rows(R - 1).Cells("Nome").Value = ""
            dgv.Rows(R - 1).Cells("Telefono").Value = ""
            dgv.Rows(R - 1).Cells("Indirizzo").Value = ""
            dgv.Rows(R - 1).Cells("Città").Value = ""
        End If
        R -= 1
        carica()
        dgv.Rows.Clear()
        prendi()
    End Sub
    Dim tempo As Integer
    Private Sub Timer1_Tick(sender As System.Object, e As System.EventArgs) Handles Timer1.Tick
        Label6.Text = tempo
        tempo += 1
    End Sub

    Private Sub txtCognome_TextChanged(sender As System.Object, e As System.EventArgs) Handles txtCognome.TextChanged
        Timer1.Start()
        MessageBox.Show("")
    End Sub
End Class
